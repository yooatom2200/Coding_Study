#include<stdio.h>
int main() {
	int a;
	scanf("%d", &a);
	while (a) {
		--a;
		printf("%d\n", a);
	}

	return 0;
}
