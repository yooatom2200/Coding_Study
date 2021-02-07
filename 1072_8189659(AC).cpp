#include<stdio.h>
int main() {
	int a,b;
	scanf("%d", &a);
	for (int i = 0; i < a; i++) {
		scanf("%d", &b);
		printf("%d\n", b);
	}
	return 0;
}
