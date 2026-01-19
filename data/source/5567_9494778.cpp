#include <iostream>
#define Mx 99999999
using namespace std;
int N,M,ar[550][550],a,b,check[550],Mincheck[550],Min,Cnt;
int main()
{
	cin>>N>>M;
	
	for(int x=0; x<=N; x++)
		for(int y=0; y<=N; y++)ar[x][y]=Mx;
		
	for(int x=0; x<M; x++)
	{
		cin>>a>>b;
		ar[a][b]=1;
		ar[b][a]=1;
	}
	for(int x=2; x<=N; x++) Mincheck[x]=Mx;
	Mincheck[1]=0;
	Mincheck[0]=1;
	for(int x=1; x<=N; x++)
	{
		int S=0; 
		Min=Mx;
		for(int y=1; y<=N; y++)
		{
			if(check[y]!=1&&Mincheck[y]<Min)
			{
				Min=Mincheck[y];
				S=y;
			}
		}
		check[S]=1;	
		for(int z=1; z<=N; z++)
		{
			if(Mincheck[z]>Mincheck[S]+ar[S][z])
			{
				Mincheck[z]=Mincheck[S]+ar[S][z];
			}
		}
	}
	for(int x=1; x<=N; x++)
	{
		if(1<=Mincheck[x]&&Mincheck[x]<=2) Cnt++;
	}
	cout<<Cnt;
}