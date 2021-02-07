#include<stdio.h>
#include<string.h>
struct Security {
	char name[10];
	int age;
	char part;
	float key;
};
int main() {
	struct Security a;
	scanf("%s", &a.name);
	printf("%s\n", a.name);
	scanf("%d", &a.age);
	printf("%d\n", a.age);
	scanf(" %c", &a.part);
	printf("%c\n", a.part);
	scanf("%f", &a.key);
	printf("%g\n", a.key);
	return 0;
}

