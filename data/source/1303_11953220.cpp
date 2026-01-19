#include <iostream>
using namespace std;
int N,M,check[110][110];
char ar[110][110];
int dy[]={0,0,1,-1};
int dx[]={1,-1,0,0};
int T_a,T_b,C_a,C_b;

void DFS(int Y,int X)
{
	if(ar[Y][X]=='W') C_a++;
	else C_b++;
	check[Y][X]=1;
	for(int d=0; d<4; d++)
	{
		if(0<=Y+dy[d]&&Y+dy[d]<M&&0<=X+dx[d]&&X+dx[d]<N)
		{
			if(check[Y+dy[d]][X+dx[d]]!=1&&ar[Y][X]==ar[Y+dy[d]][X+dx[d]])
			{
				DFS(Y+dy[d],X+dx[d]);	
			}	
		}
	}
}

int main()
{
	cin>>N>>M; //N이 가로 
	for(int y=0; y<M; y++)
	{
		for(int x=0; x<N; x++)
		{
			cin>>ar[y][x];
		}
	}
	
	for(int y=0; y<M; y++)
	{
		for(int x=0; x<N; x++)
		{
			if(check[y][x]!=1)
			{
				C_a=0;
				C_b=0;
				DFS(y,x);
				if(ar[y][x]=='W')
				{
					T_a+=C_a*C_a;
				}
				else
				{
					T_b+=C_b*C_b;
				}
			}
		}
	}
	cout<<T_a<<" "<<T_b;
}
