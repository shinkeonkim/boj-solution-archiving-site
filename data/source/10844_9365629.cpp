#include <iostream>
using namespace std;
int N;
unsigned long long int ar[110][20];
unsigned long long int Sum;
int main()
{
	cin>>N;
	for(int x=1; x<=9; x++) ar[1][x]=1;
	for(int x=2; x<=N; x++)
	{
		for(int y=0; y<=9; y++)
		{
			if(y>0)
			{
				ar[x][y-1]+=ar[x-1][y];
				ar[x][y-1]%=1000000000;
			} 
			if(y+1<10)
			{
				ar[x][y+1]+=ar[x-1][y];
				ar[x][y+1]%=1000000000;
			}
		}
	}
	for(int x=0; x<=9; x++)
	{
		Sum+=ar[N][x];
		Sum%=1000000000;
	}
	cout<<Sum;
}