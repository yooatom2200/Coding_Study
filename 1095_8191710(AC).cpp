#include<stdio.h>
int main() {
	int a,c;
	int b[1000] = {};
	scanf("%d", &a);
	for (int i = 0; i < a; i++) {
		int d;
		scanf("%d", &d);
		b[i] = d;
	}
	c = b[0];
	for (int i = 0; i < a; i++) {
		if (c > b[i])
			c = b[i];
	}
	printf("%d", c);
	return 0;
}
