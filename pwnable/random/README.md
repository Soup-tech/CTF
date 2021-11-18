Random

> Connection
```bash
	ssh -p 2222 random@pwnable.kr (pw: guest)
```

> Hint
```
	Daddy, teach me how to use random value in programming!
```

> Here is our source code
```C
	#include <stdio.h>

	int main(){
	unsigned int random;
	random = rand();	// random value!

	unsigned int key=0;
	scanf("%d", &key);

	if( (key ^ random) == 0xdeadbeef ){
		printf("Good!\n");
		system("/bin/cat flag");
		return 0;
	}

	printf("Wrong, maybe you should try 2^32 cases.\n");
	return 0;
```

> The goal is to get "system" to run and cat the flag. Our result from XOR'ing our input and "random" must equal 0xdeadbeef
> Here, the random number generator is never seeded, thus the value of 'random' is constant.
> If we consider 0xdeadbeef as the 'ciphertext' and 'random' as the plaintext, we can deduce the key. This is known from basic cryptography and is the weakness when using just XOR 

> First determine the value of random

```ASM
	pwndbg> disass main
	Dump of assembler code for function main:
	   0x00000000004005f4 <+0>:     push   rbp
	   0x00000000004005f5 <+1>:     mov    rbp,rsp
	   0x00000000004005f8 <+4>:     sub    rsp,0x10
	   0x00000000004005fc <+8>:     mov    eax,0x0
	   0x0000000000400601 <+13>:    call   0x400500 <rand@plt>
	   0x0000000000400606 <+18>:    mov    DWORD PTR [rbp-0x4],eax
	   0x0000000000400609 <+21>:    mov    DWORD PTR [rbp-0x8],0x0
	   0x0000000000400610 <+28>:    mov    eax,0x400760
	   0x0000000000400615 <+33>:    lea    rdx,[rbp-0x8]
	   0x0000000000400619 <+37>:    mov    rsi,rdx
	   0x000000000040061c <+40>:    mov    rdi,rax
	   0x000000000040061f <+43>:    mov    eax,0x0
	   0x0000000000400624 <+48>:    call   0x4004f0 <__isoc99_scanf@plt>
	   0x0000000000400629 <+53>:    mov    eax,DWORD PTR [rbp-0x8]
	   0x000000000040062c <+56>:    xor    eax,DWORD PTR [rbp-0x4]
	   0x000000000040062f <+59>:    cmp    eax,0xdeadbeef
	   0x0000000000400634 <+64>:    jne    0x400656 <main+98>
	   0x0000000000400636 <+66>:    mov    edi,0x400763
	   0x000000000040063b <+71>:    call   0x4004c0 <puts@plt>
	   0x0000000000400640 <+76>:    mov    edi,0x400769
	   0x0000000000400645 <+81>:    mov    eax,0x0
	   0x000000000040064a <+86>:    call   0x4004d0 <system@plt>
	   0x000000000040064f <+91>:    mov    eax,0x0
	   0x0000000000400654 <+96>:    jmp    0x400665 <main+113>
	   0x0000000000400656 <+98>:    mov    edi,0x400778
	   0x000000000040065b <+103>:   call   0x4004c0 <puts@plt>
	   0x0000000000400660 <+108>:   mov    eax,0x0
	   0x0000000000400665 <+113>:   leave  
	   0x0000000000400666 <+114>:   ret    
	End of assembler dump.
```
> The value from 'rand' is returned to eax. Later eax stores the value into [rbp-0x4]
```ASM
	pwndbg> x/xw $rbp-0x4
	0x7fffdaebea1c: 0x6b8b4567
```
0x6b8b4567 = 0d1804289383
> With this value we can 0x6b8b4567 ^ 0xdeadbeef = key
> I use python3 to figure out the key
key = 3039230856

> Running random and inputting the key and we get the flag
```bash
	./random
	3039230856
```

> flag
```
	Good!
	Mommy, I thought libc random is unpredictable...
```

> New things I learned
```
	Nothing, this problem was to easy with my current skillset
```