#include <iostream>
using namespace std;
int N,ar[20][20],a,b;
int main()
{
	cin>>N;
	for(int x=1; x<=N; x++)
	{
		cin>>a>>b;
		ar[x][x+a-1]=b;
	}
	for(int x=1; x<=N; x++)
		for(int y=x; y<=N; y++)
			for(int z=y+1; z<=N; z++)
				for(int w=z; w<=N; w++)
				{
					if(ar[x][w]<ar[x][y]+ar[z][w])
					{
						ar[x][w]=ar[x][y]+ar[z][w];
					}				
				}
	cout<<ar[1][N];
}