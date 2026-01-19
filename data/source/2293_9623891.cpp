#include <iostream>
using namespace std;
int N,K,ar[110],D[11000];
int main()
{
	cin>>N>>K;
	for(int x=0; x<N; x++)cin>>ar[x];
	D[0]=1;
	for(int y=N-1; y>-1; y--)
	{
		for(int x=1; x<=K; x++)
		{	
			if(x-ar[y]>=0)
			{
				D[x]+=D[x-ar[y]];
			}
		}
	}
	
	//for(int x=1; x<=K; x++) cout<<D[x]<<" ";
	cout<<D[K];
}