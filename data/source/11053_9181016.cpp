#include <iostream>
using namespace std;
int N,ar[1100],check[1100],Max=1;
int main()
{
	cin>>N;
	for(int x=0; x<N; x++)cin>>ar[x];
	for(int x=0; x<N; x++)
	{
		check[x]=1;
		for(int y=0; y<x; y++)
		{
			if(ar[y]<ar[x]&&check[y]+1>check[x])
			{
				check[x]=check[y]+1;
				if(check[x]>Max) Max=check[x];
			}
		}
	}
	cout<<Max;
}