#include<stdio.h>
int main() {
	char a,b;
	do {
		scanf("%c%c", &a,&b);
		printf("%c\n", a);
	} while (a != 'q');
	return 0;
}
