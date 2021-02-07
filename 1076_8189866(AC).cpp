#include<stdio.h>
int main() {
	char a,b = 'a';
	scanf("%c", &a);
	do {
		printf("%c ", b);
		b++;
	} while (a+1 != b);

	return 0;
}
