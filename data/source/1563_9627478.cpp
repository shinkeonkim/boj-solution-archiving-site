#include <iostream>
#define Mod 1000000
using namespace std;
unsigned long long int N,D[1100][5][5];
int main()
{
	cin>>N;
	D[1][0][0]=D[1][1][1]=D[1][0][2]=1;
	D[1][0][3]=0;
	for(int i=2; i<=N; i++)
	{
		 D[i][0][0]=(D[i-1][0][0]+D[i-1][0][2]+D[i-1][0][3])%Mod;
		 D[i][0][1]=0;
		 D[i][0][2]=D[i-1][0][0];
		 D[i][0][3]=D[i-1][0][2];
		 
		 D[i][1][0]=(D[i-1][1][0]+D[i-1][1][1]+D[i-1][1][2]+D[i-1][1][3])%Mod;
		 D[i][1][1]=(D[i-1][0][0]+D[i-1][0][2]+D[i-1][0][3])%Mod;
		 D[i][1][2]=(D[i-1][1][0]+D[i-1][1][1])%Mod;
		 D[i][1][3]=D[i-1][1][2];
	}
	unsigned long long int ans=0;
	for(int x=0; x<2; x++)
	{
		for(int y=0; y<4; y++)
		{
			ans+=D[N][x][y];
			ans%=Mod;
		}
	}
	cout<<ans;
	
}