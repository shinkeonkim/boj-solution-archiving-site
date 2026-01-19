#include <iostream>
#include <cstdio>
using namespace std;
int Cnt,N,M,a,b,ar[2200],D[2200][2200];
int f(int x,int y)
{
	Cnt++;
	if(D[x][y]) return D[x][y];
	else if(x==y) return D[x][y]=1;
	else if(y==x+1)
	{
		if(ar[y]==ar[x]) return D[x][y]=1;
		else return D[x][y]=2;
	}
	else if(x<y) 
	{
		if(ar[x]!=ar[y]) return D[x][y]=2;
		else return D[x][y]=f(x+1,y-1);
	}
	else return D[x][y]=2;
}
int main()
{
	cin>>N;
	for(int x=1; x<=N; x++)
	{
		cin>>ar[x];
	}
	
	for(int x=1; x<=N; x++)
	{
		for(int y=x; y<=N; y++)
		{
			if(D[x][y]==0)
			{
				f(x,y);
			}
		}
	}
	cin>>M;
	for(int x=0; x<M; x++)
	{
		scanf("%d %d",&a,&b);
		if(D[a][b]!=1) printf("0\n");
		else printf("1\n");
	}
	
	//cout<<Cnt;
	/*for(int x=1; x<=N; x++)
		for(int y=1; y<=N; y++)
		{
			cout<<x<<" "<<y<<" "<<D[x][y]<<endl;
		}*/
}
