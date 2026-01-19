#include <iostream>
using namespace std;
int N,K,coin[11],Cnt;
int main()
{
	cin>>N>>K;
	for(int x=0; x<N; x++) cin>>coin[x];
	for(int x=N-1; x>=0; x--)
	{
		while(K>=coin[x])
		{
			Cnt+=K/coin[x];
			K=K%coin[x];
		}
	}
	cout<<Cnt;
}