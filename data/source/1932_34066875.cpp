#include <iostream>
using namespace std;
int N,ar[550][550];
int main()
{
	cin>>N;
	for(int y=0; y<N; y++)
	{
		for(int x=0; x<=y; x++)
		{
			cin>>ar[x][y];
		}
	}
	if(N==1) cout<<ar[0][0];
	else
	{
		ar[1][1]+=ar[0][0];
		ar[0][1]+=ar[0][0];
		for(int y=2; y<N; y++)
		{
			for(int x=0; x<=y; x++)
			{
				if(x==0)
				{
					ar[x][y]+=ar[x][y-1];
				}
				else if(x==y)
				{
					ar[x][y]+=ar[x-1][y-1];
				}
				else
				{
					if(ar[x-1][y-1]>ar[x][y-1]) ar[x][y]+=ar[x-1][y-1];
					else ar[x][y]+=ar[x][y-1];
				}
			}
		}
    int Max=0;
    for(int x=0; x<N; x++)
    {
      if(ar[x][N-1]>Max)Max=ar[x][N-1];
    }
    cout<<Max;
	}
}