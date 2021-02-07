#include<stdio.h>
int main() {
	int a,b = 0,c = 0;
	scanf("%d", &a);
	while (a > b) {
		c++;
		b += c;
	}
	printf("%d", c);
	return 0;
}
