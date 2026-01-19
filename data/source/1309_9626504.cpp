#include <iostream>
using namespace std;
int N,D[110000];
int main()
{
	cin>>N;
	D[1]=3;
	D[2]=7;
	for(int x=3; x<=N; x++)
	{
		D[x]=(D[x-1]*2+D[x-2])%9901;
	}
	cout<<D[N];
}