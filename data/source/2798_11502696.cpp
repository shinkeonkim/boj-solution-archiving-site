#include <iostream>
using namespace std;
int N,M,Max;
int ar[110];

int f(int x)
{
	return x>0?x:-x;
}
int main()
{
	cin>>N>>M;
	for(int x=0; x<N; x++) cin>>ar[x];
	for(int x=0; x<N; x++)
	{
		for(int y=x+1; y<N; y++)
		{
			for(int z=y+1; z<N; z++)
			{
				int S=ar[x]+ar[y]+ar[z];
				if(f(M-Max)>f(M-S)&&S<=M)
				{
					Max=S;
				}
			}
		}
	}
	cout<<Max;
}