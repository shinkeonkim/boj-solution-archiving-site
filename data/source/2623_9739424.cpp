#include <iostream>
#include <queue>
using namespace std;
int N,M,K,ar[1100][1100],Sum[1100],check[1100],input[1100];
queue<int> que;
int main()
{
	cin>>N>>M;
	for(int x=0; x<M; x++)
	{
		cin>>K;
		for(int y=0; y<K; y++)cin>>input[y];
		for(int y=0; y<K-1; y++)
		{
			ar[input[y]][input[y+1]]=1;
		}
	}
	for(int x=1; x<=N; x++)
	{
		for(int y=1; y<=N; y++)
		{
			Sum[x]+=ar[y][x];
		}
	}
	for(int x=1; x<=N; x++)
	{
		int A=0;
		for(int y=1; y<=N; y++)
		{
			if(Sum[y]==0&&check[y]==0) A=y;
		}
		if(A==0)
		{
			cout<<"0";
			return 0;
		}
		check[A]=1;
		que.push(A);
		for(int y=1; y<=N; y++)
		{
			if(ar[A][y]==1)
			{
				Sum[y]--;
				ar[A][y]=0;
			}
		}
	}
	while(!que.empty())
	{
		cout<<que.front()<<" ";
		que.pop();
	}
}