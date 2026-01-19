#include <iostream>
using namespace std;
int N,K,ar[1100][1100];

int main()
{
	cin>>N>>K;
	for(int n=1; n<=N+K-1; n++)
	{
		for(int k=1; k<=n; k++)
		{
			if(k==1) ar[n][k]=n;
			else if(n==k) ar[n][k]=1;
			else ar[n][k]=(ar[n-1][k-1]+ar[n-1][k])%1000000000;
		}
	}
	cout<<ar[N+K-1][N];
}