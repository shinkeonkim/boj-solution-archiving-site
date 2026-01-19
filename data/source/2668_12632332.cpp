#include <iostream>
#define Mx 999999999
using namespace std;
int N,ar[110][110],Cnt;
int main()
{
	cin>>N;
	for(int x=1; x<=N; x++)
		for(int y=1; y<=N; y++)
			ar[x][y]=Mx;
	
	for(int x=1; x<=N; x++)
	{
		int a;
		cin>>a;
		ar[x][a]=1;
	}
	for(int z=1; z<=N; z++)
		for(int x=1; x<=N; x++)
			for(int y=1; y<=N; y++)
			{
				if(ar[x][y]>ar[x][z]+ar[z][y])
				ar[x][y]=ar[x][z]+ar[z][y];
			}
	
	for(int x=1; x<=N; x++)
	{
		if(ar[x][x]!=Mx) Cnt++;
	}
	cout<<Cnt<<endl;
	for(int x=1; x<=N; x++)
	{
		if(ar[x][x]!=Mx) cout<<x<<endl;
	}
}
