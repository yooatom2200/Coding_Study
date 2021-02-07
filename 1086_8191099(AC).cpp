#include<stdio.h>
int main() {
	int h, b, c;
	scanf("%d %d %d", &h, &b, &c);
	printf("%.2f MB", (float)(((h*b*c) / 8)/1024)/1024);
	
	return 0;
}
