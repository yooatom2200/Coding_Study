#include<stdio.h>
int main() {
	int a[19][19] = {},n;
	for (int i = 0; i < 19; i++) {
		for (int j = 0; j < 19; j++) {
			int x;
			scanf("%d", &x);
			a[i][j] = x;
		}
	}
	scanf("%d", &n);
	for (int q = 0; q < n; q++) {
		int w, e;
		scanf("%d %d", &w, &e);
		for (int i = 0; i < 19; i++) {
			a[w-1][i] = !a[w-1][i];
		}
		for (int i = 0; i < 19; i++) {
			a[i][e-1] = !a[i][e-1];
		}
	}
	for (int i = 0; i < 19; i++) {
		for (int j = 0; j < 19; j++) {
			printf("%d ", a[i][j]);
		}
		printf("\n");
	}
		
	return 0;
}
