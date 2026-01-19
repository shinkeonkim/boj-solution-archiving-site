#include <iostream>
using namespace std;
int ar[101];
int check[110000];
int N,I;
int main()
{
	for(int x=1; x<=45; x++)
	{
		ar[x]=(x*(x+1))/2;
	}
	for(int x=1; x<=45; x++)
	{
		for(int y=1; y<=45; y++)
		{
			for(int z=1; z<=45; z++)
			{
				check[ar[x]+ar[y]+ar[z]]=1;
			}
		}
	}
	cin>>N;
	for(int x=0; x<N; x++)
	{
		cin>>I;
		cout<<check[I]<<endl;
	}
}