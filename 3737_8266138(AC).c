#include<stdio.h>
long long int count = 0,cp,cpc;
void jagi(long long int n) {
	count++;
	if (cp < n) {
		cp = n;
		cpc = count;
	}
	if (n == 1)
		return;
	if (n % 3 == 0)
		jagi(n / 3);
	else if (n % 3 == 1)
		jagi(5 * n - 2);
	else if (n % 3 == 2)
		jagi(5 * n - 1);
}
int main() {
	long long int n;
	scanf("%lld", &n);
	jagi(n);
	printf("%lld\n", count);
	printf("%lld %lld", cpc, cp);
	return 0;
}
