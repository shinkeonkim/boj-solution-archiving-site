#include <iostream>
using namespace std;
int N,M,K,a,b,ar[110];
int main()
{
	cin>>N>>M;
	for(int x=1; x<=N; x++)ar[x]=x;
	for(int x=0; x<M; x++)
	{
		cin>>a>>b;
		K=ar[a];
		ar[a]=ar[b];
		ar[b]=K;
	}
	for(int x=1; x<=N; x++)cout<<ar[x]<<" ";
}