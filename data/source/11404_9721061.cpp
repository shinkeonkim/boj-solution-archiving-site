#include <iostream>
#define Mx 9999999
using namespace std;
int N,M,a,b,c,ar[110][110];
int main()
{
	cin>>N>>M;
	
	for(int x=1; x<=N; x++)
		for(int y=1; y<=N; y++)
		{
			ar[x][y]=Mx;
		}
		
	for(int x=0; x<M; x++)
	{
		cin>>a>>b>>c;
		if(ar[a][b]>c) ar[a][b]=c;
	}
	
	for(int z=1; z<=N; z++)
		for(int x=1; x<=N; x++)
			for(int y=1; y<=N; y++)
			{
				if(ar[x][y]>ar[x][z]+ar[z][y])
				{
					ar[x][y]=ar[x][z]+ar[z][y];
				}
			}
			
	for(int y=1; y<=N; y++)
	{
		for(int x=1; x<=N; x++)
		{
			if(y==x) cout<<"0 ";
			else if(ar[y][x]!=Mx) cout<<ar[y][x]<<" ";
			else cout<<"0 ";
		}cout<<"\n";
	}
}