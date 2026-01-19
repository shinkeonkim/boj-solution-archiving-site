#include <iostream>
using namespace std;
int memo[400];
int f(int x)
{
	if(memo[x]) return memo[x];
	else if(x==0) return memo[x]=0;
	else if(x==1) return memo[x]=1;
	else return memo[x]=f(x-1)+f(x-2);
}
int main()
{
	int n;
	scanf("%d",&n);
	printf("%d",f(n));
}