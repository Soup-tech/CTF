#include <stdio.h>
#include <string.h>

int main(int argc, char * argv[]) {
	// Two arguments
	if (argc != 2) {
		puts("Wrong number of params");
		return 0;
	}
	if (strcmp(argv['A'],"\x20\x0a\x0d") != 0) {
		puts("Wrong value");
		return 0;
	}

	puts("Made it after conditionals");

	return 0;
}