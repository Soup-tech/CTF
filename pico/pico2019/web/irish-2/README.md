# Irish-Name-Repo 2

### Connection
```
	https://jupiter.challenges.picoctf.org/problem/64649/
```

### Description
```
	Someone has bypassed the login before, and now it's being strengthened. Try to see if you can still login!
```

### Hint
```
	The password is being filtered.
```

### Solving the problem
Inputting <i>admin:admin</i> returns a <b>LOGIN FAILED</b>.<br>
Now when we input <i>admin:'</i> we get a <b>SQLi Detected</b>.<br>
<br>
I suspect that the SQL query is the same as before:
```SQL
	SELECT * FROM users WHERE username='$username' AND password='$password'
```
<br>
Based on the hint provided for the problem, apostrophes are my primary suspect as to which characters are being filtered.<br>
After catching the request in BurpSuite, I began trying variations of SQL injections. I also began some research on SQLi that bypassed logins. Alas, I could not find any that didn't contain an apostrophe. However, after some time I realized that there is more than one field I could try injecting into.<br>
The first injection I performed in the username field was <i>admin'--:password</i> which would perform the following query:
```SQL
	SELECT * FROM users WHERE username='admin''-- AND password='$password'
```

### Flag
```
	picoCTF{m0R3_SQL_plz_aee925db}
```

### Things I learned
Always test all the available input fields when testing for SQLi.<br>
Because of the hint, I thought I would have to try some variation of <b>' OR 1=1-- </b>.
