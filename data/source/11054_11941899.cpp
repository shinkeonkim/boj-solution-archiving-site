#include <iostream>
using namespace std;
int N,ar[1100],DP1[1100],DP2[1100],Max=-1;
int main()
{
	cin>>N;
	for(int x=0; x<N; x++) cin>>ar[x];
	for(int x=0; x<N; x++)
	{
		if(DP1[x]==0) DP1[x]=1;
		
		for(int y=0; y<x; y++)
		{
			if(ar[y]<ar[x] && DP1[y]+1>DP1[x])
			{
				DP1[x]=DP1[y]+1;
			}
		}
	}
	for(int x=N-1; x>-1; x--)
	{
		if(DP2[x]==0) DP2[x]=1;
		
		for(int y=x-1; y>-1; y--)
		{
			if(ar[y]>ar[x] && DP2[y]<DP2[x]+1)
			{
				DP2[y]=DP2[x]+1;
			}
		}
	}
	
	for(int x=0; x<N; x++)
	{
		if(Max<DP1[x]+DP2[x]) Max=DP1[x]+DP2[x];
	}
	cout<<Max-1;
}