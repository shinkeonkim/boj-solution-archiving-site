#include <iostream>
using namespace std;
int N,K,ar[1100][1100];
int f(int n,int k)
{
	if(ar[n][k]) return ar[n][k];
	else if(n<k) return ar[n][k]=0;
	else if(k==1) return ar[n][k]=n;
	else if(n==k||k==0) return ar[n][k]=1;
	else return ar[n][k]=(f(n-1,k)+f(n-1,k-1))%10007;
}
int main()
{
	cin>>N>>K;
	cout<<f(N,K);
}