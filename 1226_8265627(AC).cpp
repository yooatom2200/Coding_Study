#include<stdio.h>
int main() {
	int cNumber[7];
	int jNumber[6];
	int count = 0,bonus = 0;
	for (int i = 0; i < 7; i++)
		scanf("%d", &cNumber[i]);
	for (int i = 0; i < 6; i++)
		scanf("%d", &jNumber[i]);
	for (int i = 0; i < 6; i++) {
		for (int j = 0; j < 6; j++) {
			if (cNumber[i] == jNumber[j])
				count++;
		}
			if (cNumber[6] == jNumber[i])
				bonus++;
	}
	switch (count) {
	case 1: 
	case 2:
		printf("0");
		break;
	case 3:
		printf("5");
		break;
	case 4:
		printf("4");
		break;
	case 5:
		if (bonus == 1)
			printf("2");
		else
			printf("3");
		break;
	case 6:
		printf("1");
		break;
	}
	return 0;
}

