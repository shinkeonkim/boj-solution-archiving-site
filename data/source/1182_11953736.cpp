#include <iostream>
using namespace std;
int N,S,check[22],ar[22],ans;
void g()
{
	int K=0,d=0;
	for(int x=0; x<N; x++)
	{
		if(check[x]==1)
		{
			d=1;
			K+=ar[x];
		}		
	}
	if(K==S&&d==1) ans++;
}
void DFS(int M)
{
	if(M==N-1)
	{
		for(int x=0; x<2; x++)
		{
			check[M]=x;
			g();
		}
	}
	else
	{
		for(int x=0; x<2; x++)
		{
			check[M]=x;
			DFS(M+1);
		}
	}
}
int main()
{
	cin>>N>>S;
	for(int x=0; x<N; x++) cin>>ar[x];
	DFS(0);
	cout<<ans; 
}