#include <stdio.h>
#include <stdlib.h>

int main() {
	int passcode1;
	int passcode2;

	printf("enter passcode1: ");
	scanf("%d", passcode1);
	fflush(stdin);

	printf("enter passcode2: ");
	scanf("%d", passcode2);

	printf("checking...\n");
	if (passcode1 == 388150 && passcode2 == 13371337) {
		printf("correct\n");
		return 0;
	}


	return 0;
}