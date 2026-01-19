#include <iostream>
using namespace std;
int N,K,Sum,ar[3][8];
int main()
{
	cin>>N>>K;
	for(int x=0; x<N; x++)
	{
		int a,b;
		cin>>a>>b;
		ar[a][b]++;
	}
	for(int x=0; x<2; x++)
	{
		for(int y=1; y<7; y++)
		{
			Sum+=ar[x][y]/K;
			if(ar[x][y]%K>0)Sum++;
		}
	}
	cout<<Sum;
}