#include <stdio.h>

int main(void) {
	int c;
	if ((c = getchar()) != EOF) {
		printf("Got %c; enter some new data\n", c);
		fflush(stdin);
	}
	if ((c = getchar()) != EOF) {
		printf("Got %c\n", c);
	}

	return 0;
}