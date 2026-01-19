#include <iostream>
using namespace std;
int N,K,ar[1100][1100];
int f(int n,int k)
{
	if(ar[n][k]) return ar[n][k];
	else if(n/2<k) return 0;
	else if(k==1) return n;
	else return ar[n][k]=(f(n-1,k)+f(n-2,k-1))%1000000003;
}
int main()
{
	cin>>N>>K;
	cout<<f(N,K);	
}