#include <iostream>
#define Mx 99999999
using namespace std;
int N,A,B,M,a,b;
int ar[110][110];
int main()
{
	cin>>N>>A>>B>>M;
	for(int x=1; x<=N; x++)
		for(int y=1; y<=N; y++) ar[x][y]=Mx;
		
	for(int x=0; x<M; x++)
	{
		cin>>a>>b;
		ar[a][b]=1;
		ar[b][a]=1;
	}
	
	for(int z=1; z<=N; z++)
		for(int x=1; x<=N; x++)
			for(int y=1; y<=N; y++)
			{
				if(ar[x][y]>ar[x][z]+ar[z][y]) ar[x][y]=ar[x][z]+ar[z][y];
			}
	if(ar[A][B]!=Mx) cout<<ar[A][B];
	else cout<<"-1";
}