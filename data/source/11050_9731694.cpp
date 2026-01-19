#include <iostream>
using namespace std;
int N,K,ar[110][110];
int f(int n,int k)
{
	if(ar[n][k]) return ar[n][k];
	else if(n<k) return ar[n][k]=0;
	else if(k==0||n==k) return ar[n][k]=1;
	else if(k==1) return ar[n][k]=n;
	else return ar[n][k]=f(n-1,k-1)+f(n-1,k);
}
int main()
{
	cin>>N>>K;
	cout<<f(N,K);
}