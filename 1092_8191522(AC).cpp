#include<stdio.h>
int main() {
	int a, b, c, i;
	scanf("%d %d %d", &a, &b, &c);
	i = (a > b ? a : b) > c ? (a > b ? a : b) : c;
	while (i % a != 0 || i % b != 0 || i % c != 0)
		i++;
	printf("%d", i);
	return 0;
}
