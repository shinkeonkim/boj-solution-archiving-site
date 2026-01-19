#include <iostream>
#include <algorithm>
using namespace std;
int T,N,A[110000][3],D[110000][3],Max;
int main()
{
	cin>>T;
	for(int x=0; x<T; x++)
	{
		Max=0;
		cin>>N;
		for(int y=0; y<2; y++)
		{
			for(int x=0; x<N; x++)cin>>A[x][y];
		}
		
		D[0][0]=A[0][0];
		D[0][1]=A[0][1];
		D[1][0]=A[0][1]+A[1][0];
		D[1][1]=A[1][1]+A[0][0];
		Max=max(Max,max(max(D[0][0],D[0][1]),max(D[1][0],D[1][1])));
		for(int x=2; x<N; x++)
		{
			D[x][0]=max(D[x-2][1],D[x-1][1])+A[x][0];
			D[x][1]=max(D[x-2][0],D[x-1][0])+A[x][1];
			Max=max(Max,max(D[x][0],D[x][1]));
		}
		cout<<Max<<endl;
		for(int y=0; y<2; y++)
		{
			for(int x=0; x<N; x++)
			{
				A[x][y]=0;
				D[x][y]=0;
			}
		}
	}
}