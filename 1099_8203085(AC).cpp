#include<stdio.h>
int main() {
	int maze[10][10] = {};
	int px = 1, py = 1;
	for (int i = 0; i < 10; i++) {
		for (int j = 0; j < 10; j++) {
			scanf("%d", &maze[i][j]);
		}
	}
	while (!(px >= 9 || py >= 9)){
		if (maze[px][py] != 2) {
			maze[px][py] = 9;
		}
		else {
			maze[px][py] = 9;
			break;
		}
			maze[px][py] = 9;
		if (maze[px][py+1] == 0)
			py += 1;
		else if (maze[px][py+1] == 1)
			px += 1;
	}
	for (int i = 0; i < 10; i++) {
		for (int j = 0; j < 10; j++) {
			printf("%d ", maze[i][j]);
		}
		printf("\n");
	}

	return 0;
}

