#include <iostream>
using namespace std;
int N,ar[5],K;
int f(int A,int B)
{
	return B>0?f(B,A%B):A;
}
int main()
{
	cin>>N;
	for(int x=0; x<N; x++)  cin>>ar[x];
	K=ar[0];
	for(int x=1; x<N; x++)
	{
		K=f(K,ar[x]);
	}
	for(int x=1; x<=K; x++)
	{
		if(K%x==0) cout<<x<<endl;
	}
} 