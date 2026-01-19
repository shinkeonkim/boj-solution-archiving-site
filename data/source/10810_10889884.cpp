#include <iostream>
using namespace std;
int N,M,a,b,c;
int ar[110];
int main()
{
	cin>>N>>M;
	for(int x=0; x<M; x++)
	{
		cin>>a>>b>>c;
		for(int x=a; x<=b; x++)
		{
			ar[x]=c;
		}
	}
	for(int x=1; x<=N; x++)
	{
		cout<<ar[x]<<" ";
	}
}