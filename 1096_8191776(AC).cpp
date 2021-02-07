#include<stdio.h>
int main() {
	int a[19][19] = {}, b;
	scanf("%d", &b);
	for (int i = 0; i < b; i++){
		int x, y;
		scanf("%d %d", &x, &y);
		a[x-1][y-1] = 1;
	}
	for (int i = 0; i < 19; i++) {
		for (int j = 0; j < 19; j++) {
			if (a[i][j] == 1)
				printf("1 ");
			else
				printf("0 ");
		}
		printf("\n");
	}
		
	return 0;
}
