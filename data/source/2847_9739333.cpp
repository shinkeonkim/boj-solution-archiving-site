#include <iostream>
using namespace std;
int N,ar[110],Cnt;
int main()
{
	cin>>N;
	for(int x=1; x<=N; x++)cin>>ar[x];
	for(int x=1; x<=N; x++)
	{
		for(int y=1; y<=N; y++)
		{
			for(int z=y+1; z<=N; z++)
			{
				if(ar[y]>=ar[z])
				{
					//cout<<y<<" "<<z<<" "<<ar[y]<<" "<<ar[z]<<endl;
					Cnt+=ar[y]-ar[z]+1;
					ar[y]=ar[z]-1;
				}
			}
		}
	}
	cout<<Cnt;
}