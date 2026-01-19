#include <iostream>
using namespace std;
int N,M;
char A[22][22],B[22][22];

int main()
{
	cin>>N>>M;
	for(int y=0; y<N; y++)
	{
		for(int x=0; x<M; x++)
		{
			cin>>A[y][x];
		}
	}
	
	for(int y=0; y<N; y++)
	{
		for(int x=0; x<2*M; x++)
		{
			cin>>B[y][x];
		}
	}
	
	for(int y=0; y<N; y++)
	{
		for(int x=0; x<M; x++)
		{
			if(A[y][x]!=B[y][2*x]||A[y][x]!=B[y][2*x+1])
			{
				cout<<"Not Eyfa";
				return 0;
			}
		}
	}
	cout<<"Eyfa";
}
