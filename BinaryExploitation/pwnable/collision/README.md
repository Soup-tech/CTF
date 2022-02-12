# Collision

## Connection
```bash
	ssh col@pwnable.kr -p2222 (pw:guest)
```

## Hint
```
	Daddy told me about cool MD5 hash collision today.
	I wanna do something like that too!
```

## Code
```C
#include <stdio.h>
#include <string.h>

unsigned long hashcode = 0x21DD09EC;

unsigned long check_password(const char* p){
        int * ip = (int *) p;
        int i;
        int res = 0;

        for (i = 0; i < 5; i++){
                res += ip[i];
        }
        printf("0x%08x\n", res);
        return res;
}

int main(int argc, char * argv[]){
        if(argc<2){
                printf("usage : %s [passcode]\n", argv[0]);
                return 0;
        }
        if(strlen(argv[1]) != 20){
                printf("passcode length should be 20 bytes\n");
                return 0;
        }

        if(hashcode == check_password( argv[1] )){
                system("/bin/cat flag");
                return 0;
        }
        else
                printf("wrong passcode.\n");
        return 0;
}

```
Our input must be twenty characters (or 20 bytes).<br>
Within the <b>check_password</b> function, our argv[1] is casted into an integer pointer. In 32-bit architectures, integers are 4 bytes long. This means our input will be broken into 5 segments. Each segment will be added into <b>res</b> and the total must equal hashcode.<br>
The value <b>0x21DD09EC</b> is <b>0d568134124</b>.<br>

## Procedure
568134124 // 5 = 113626824 => 0x6c5cec8 <br>
113626824 * 4 = 454507296 (First 16 Bytes)<br>
568134124 - 454507296 = 113626828 => 0x6c5cecc (Last 4 Bytes)<br>
Our final payload looks like this:
```Python
	python -c 'print "\xc8\xce\xc5\x06"*4 + \xcc\xce\xc5\x06"'
```
This cannot be loaded directly into <b>col</b> so I will write a exploitation script using <b>pwntools</b>.
```Python
	#!/usr/bin/env python3

	from pwn import *

	# Payload
	payload = p32(0x6c5cec8)*4 + p32(0x6c5cecc)

	### Connection
	# username: col
	# Hostname: pwnable.kr (You can also use the IP: 128.61.240.205; I got this with dig)
	# Password: guest
	# Port: 2222
	conn = ssh('col','pwnable.kr',password='guest',port=2222)

	### Run the remote program
	# Executable to run: col
	# Argument list: col (name of the executable), payload
	program = conn.process(executable='./col', argv=['col',payload])

	# Grab the returned output
	flag = program.recv()
	print(flag.decode())

	program.close()
	conn.close()
```

## Flag
```
	daddy! I just managed to create a hash collision :)
```

## What I Learned
I need to learn pwntools better. This Python module seems incredibly useful when writing custom exploit scripts.<br>
<a href="https://python3-pwntools.readthedocs.io/en/latest/">pwntools Documentation</a><br>