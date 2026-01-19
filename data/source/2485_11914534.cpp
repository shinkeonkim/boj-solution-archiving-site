#include <iostream>
#include <algorithm>
using namespace std;
long long N,ar[110000];
long long K,ans;
long long f(long long A, long long B)
{
	return B>0?f(B,A%B):A;
}
int main()
{
	cin>>N;
	for(int x=0; x<N; x++)
	{
		cin>>ar[x];
	}
	sort(ar,ar+N);
	K=ar[1]-ar[0];
	for(int x=2; x<N; x++)
	{
		K=f(K,ar[x]-ar[x-1]);
	}
	for(int x=1; x<N; x++)
	{
		ans+=(ar[x]-ar[x-1])/K-1;
	}
	cout<<ans;
}