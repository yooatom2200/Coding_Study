#include<stdio.h>
int main() {
	int a;
	scanf("%d", &a);
	int b[23] = {};
	for (int i = 0; i < a; i++) {
		int x;
		scanf("%d", &x);
		b[x-1]++;
	}
	for (int i = 0; i < 23; i++) {
		printf("%d ", b[i]);
	}
}
