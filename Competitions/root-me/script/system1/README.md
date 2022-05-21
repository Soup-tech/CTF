# System 1

## Reads
[Dangers of SUID Shell Scripts by Thomas Akin](https://repository.root-me.org/Administration/Unix/EN%20-%20Dangers%20of%20SUID%20Shell%20Scripts.pdf?_gl=1*1wkxtlx*_ga*MTAzODI2Njg3OC4xNjUyNzQ4ODAx*_ga_SRYSKX09J7*MTY1Mjc0ODgwMS4xLjEuMTY1Mjc0ODk3My4w)
[Set-UID Privilege Program](https://repository.root-me.org/Administration/Unix/EN%20-%20SUID%20Privileged%20Programs.pdf?_gl=1*13ib2d3*_ga*MTAzODI2Njg3OC4xNjUyNzQ4ODAx*_ga_SRYSKX09J7*MTY1Mjc0ODgwMS4xLjEuMTY1Mjc0OTg4OS4w)

## Source Code
```C
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

int main(void) {
	setreuid(geteuid(), geteuid());
	system("ls /challenge/app-script/ch11/.passwd");
	return 0;
}
```
This application was compiled and given the SUID bit.

## Solution
You can write a small bash script named "ls" to perform any action as the privileged user. Then prepend the path to this bash script to the PATH environment variable. When you run the program, your "ls" bash script will execute.
