#include <iostream>
#include <algorithm>
using namespace std;
int N,ar[1100],DP[1100];
int main()
{
	cin>>N;
	for(int x=1; x<=N; x++) cin>>ar[x];
	for(int x=1; x<=N; x++)
	{
		int A=max(ar[x],DP[x]);
		for(int y=0; x+y<=N; y++)
		{
			if(DP[x+y]<A+ar[y])
			{
				DP[x+y]=A+ar[y];
			}
		}
	}
	cout<<DP[N];
}