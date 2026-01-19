#include <iostream>
#include <vector>
using namespace std;
int N,M,a,b,cnt,check[1100];
vector < vector <int> > E(1100);

void dfs(int n)
{
	for(int x=0; x<E[n].size(); x++)
	{
		if(check[E[n][x]]==0)
		{
			check[E[n][x]]=1;
			dfs(E[n][x]);
		}
	}	
}

int main()
{
	cin>>N>>M;
	for(int x=0; x<M; x++)
	{
		cin>>a>>b;
		E[a].push_back(b);
		E[b].push_back(a);
	}
	for(int x=1; x<=N; x++)
	{
		if(check[x]==0)
		{
			cnt++;
			dfs(x);
		}
	}
	cout<<cnt;
}