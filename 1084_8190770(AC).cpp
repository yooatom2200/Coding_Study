#include<stdio.h>
int main() {
	int a, b, c, count = 0;
	scanf("%d %d %d", &a, &b, &c);
	for (int i = 0; i < a; i++) {
		for (int j = 0; j < b; j++) {
			for (int h = 0; h < c; h++) {
				printf("%d %d %d\n", i, j, h);
				count++;
			}
		}
	}
	printf("%d", count);
	return 0;
}
