#include <iostream>
using namespace std;
int N,check[1100][11],Sum;
int main()
{
	cin>>N;
	for(int x=0; x<10; x++)check[1][x]=1;
	for(int y=2; y<=N; y++)
	{
		Sum=0;
		for(int x=0; x<10; x++)
		{
			Sum+=check[y-1][x];
			check[y][x]=Sum%10007;
		}
	}
	Sum=0;
	for(int x=0; x<10; x++)
	{
		Sum+=check[N][x];
		Sum%=10007;
	}
	cout<<Sum%10007;
}