#include<stdio.h>
int main() {
	int a;
	scanf("%d", &a);
	int b[1000] = {};
	for (int i = 0; i < a; i++) {
		int d;
		scanf("%d", &d);
		b[i] = d;
	}
	for (int i = a; i > 0; i--) {
		printf("%d ", b[i - 1]);
	}
	return 0;
}
