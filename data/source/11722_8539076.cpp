#include <iostream>
using namespace std;
int N,ar[1100],DP[1100],Max;
int main()
{
	cin>>N;
	for(int x=0; x<N; x++) cin>>ar[x];
	for(int x=0; x<N; x++)
	{
		if(DP[x]==0) DP[x]=1;
		
		for(int y=0; y<x; y++)
		{
			if(ar[y]>ar[x] && DP[y]+1>DP[x])
			{
				DP[x]=DP[y]+1;
			}
		}
	}
	for(int x=0; x<N; x++)
	{
		if(Max<DP[x]) Max=DP[x];
	}
	cout<<Max;
}