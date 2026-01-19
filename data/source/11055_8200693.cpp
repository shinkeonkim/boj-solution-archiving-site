#include <iostream>
using namespace std;
int N,ar[1100],D[1100],Max;
int main()
{
	cin>>N;
	for(int x=0; x<N; x++)
	{
		cin>>ar[x],D[x]=ar[x];
		if(Max<ar[x]) Max=ar[x];
	}
	for(int x=0; x<N; x++)
	{
		for(int y=0; y<x; y++)
		{
			if(ar[x]>ar[y])
			{
				if(D[x]<D[y]+ar[x])
				{
					D[x]=D[y]+ar[x];
					if(Max<D[x])Max=D[x];
				}
			}
		}
	}
	cout<<Max;
}