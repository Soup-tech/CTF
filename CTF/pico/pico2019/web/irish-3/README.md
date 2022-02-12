# Irish-Name-Repo 3

### Connection
```
	https://jupiter.challenges.picoctf.org/problem/54253/
```

### Description
```
	Try to see if you can login as admin!
```

### Hint
```
	Seems like the password is encrypted.
```

### Solving the Problem
When navigating to the login portal we are only presented with one input field.<br>
This time however because we cannot enter anything into the username field, I suspect the query looks something like:
```SQL
	SELECT * FROM users WHERE password='$password'
```
First, tryping <i>admin</i> yields a <b>Login Failed.</b><br>
Next, trying <i>'</i> does not return anything. It might possible to perform a SQLi. When trying <i>' OR 1=1-- </i> nothing is returned.<br>
<br>
Capturing the request in BurpSuite we see a parameter in the POST request is <i>debug</i>. This parameter is assigned a value of 0 by default, however when changing it to 1 we get back
```PHP
	<pre>password: admin
		SQL query: SELECT * FROM admin where password = 'nqzva'
	</pre>
	<h1>Login failed.</h1>
```
Odd looking password. This probably means that my input is being encrypted before the query is made. One of two things might be happening:<br>
1. The password in the database is stored in this encrypted version. When I submit the query the encrypted password in the database is being compared against the submitted password.<br>
2. The password is being decrypted and then compared against the cleartext password in the database. <br>
Option 1 probably the most likely scenario because modern day login forms work in a similar way. Before anything though I need to figure out the encryption scheme.<br>
After approximatly 30 seconds, I have cracked the encryption. This is a ROT13 encryption scheme.<br>
<br>
At first I thought I had to guess the password. After a few tries I decided to write a small brute forcing script: <a href="ex.py">ex.py</a>.<br>
While that was running I decided to go back to trying SQLi. Inputting <i>' OR 1=1-- </i> returned 
```SQL
	SQL query: SELECT * FROM admin where password = '' BE 1=1--'
```


The next logical thing would be to try <i>' BE 1=1-- </i> since that was the ROT13 version. This got me the flag. <br>
To bad, I really like writting custom exploits (not that a brute forcer is much of an exploit)<br>

### Flag
```
	picoCTF{3v3n_m0r3_SQL_7f5767f6}
```
### Things I learned
Great resource for SQLI
https://netsparker.com/blog/web-security/sql-injection-cheat-sheet/
