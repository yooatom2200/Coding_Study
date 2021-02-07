#include<stdio.h>
int main() {
	int a, b, n;
	scanf("%d %d %d", &a, &b, &n);
	printf("%d", (a + b * n)-b);
	return 0;
}
