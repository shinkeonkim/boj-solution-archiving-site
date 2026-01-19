#include <iostream>
using namespace std;
int N,ar[220],D[220],Max=1;
int main()
{
	cin>>N;
	for(int x=0; x<N; x++)
	{
		cin>>ar[x];
		D[x]=1;
	}
	for(int x=0; x<N; x++)
	{
		for(int y=0; y<x; y++)
		{
			if(ar[y]<ar[x]&&D[y]+1>D[x])
			{
				D[x]=D[y]+1;
			}
		}
		if(D[x]>Max)Max=D[x];
	}
	cout<<N-Max;
}