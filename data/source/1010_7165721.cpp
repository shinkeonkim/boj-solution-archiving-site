#include <iostream>
using namespace std;
long long dp[50][50];
int T,a,b;
long long nCr(int n, int r)
{
	if(dp[n][r]) return dp[n][r];
	else if(n==r) return dp[n][r]=1;
	else if(r==1) return dp[n][r]=n;
	else return dp[n][r]=nCr(n-1,r)+nCr(n-1,r-1);
}
int main()
{
	cin>>T;
	for(int x=0; x<T; x++)
	{
		cin>>a>>b;
		cout<<nCr(b,a)<<endl;
	}
}