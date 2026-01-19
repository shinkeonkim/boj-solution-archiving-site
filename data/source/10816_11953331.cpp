#include <iostream>
#include <map>
#include <cstdio>
using namespace std;
int N,m,ar[550000],Q[550000];
map <int,int> M;
int main()
{
	scanf("%d",&N);
	for(int x=0; x<N; x++) scanf("%d",&ar[x]);
	scanf("%d",&m);
	for(int x=0; x<m; x++) scanf("%d",&Q[x]);
	for(int x=0; x<N; x++)
	{
		if(M.find(ar[x])!=M.end())
		{
			M[ar[x]]=M[ar[x]]+1;
		}
		else 
		{
			M[ar[x]]=1;
		}
	}
	for(int x=0; x<m; x++)
	{
		if(M.find(Q[x])!=M.end())
		{
			printf("%d ",M[Q[x]]);
		}
		else printf("0 ");
	}
}