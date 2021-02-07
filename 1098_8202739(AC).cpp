#include<stdio.h>
int main() {
	int h, w, n, i, d, x, y;
	int a[100][100] = {};
	scanf("%d %d", &h, &w);
	scanf("%d", &n);
	for (int f = 0; f < n; f++) {
		scanf("%d %d %d %d", &i, &d, &x, &y);
		for (int t = 0; t < i; t++) {
			if (d == 0) {
				a[x - 1][y - 1 + t] = 1;
			}
			else if (d == 1) {
				a[x - 1 + t][y - 1] = 1;
			}
		}
	}
	for (int t = 0; t < h; t++) {
		for (int k = 0; k < w; k++) {
			printf("%d ", a[t][k]);
		}
		printf("\n");
	}

	return 0;
}

