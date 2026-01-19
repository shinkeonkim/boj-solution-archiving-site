#include <iostream>
using namespace std;
int N=7369000,Cnt,K;
bool ar[9900000];
int main()
{
	cin>>K;
	for(int x=2; x<=N; x++)ar[x]=true;
	
	for(int x=2; x<=N; x++)
	{
		if(ar[x])
		{
			Cnt++;
			for(int y=x+x; y<=N; y=y+x)
			{
				ar[y]=false;
			}
			if(Cnt==K)
			{
				cout<<x;
				return 0;
			}
		}
	}
}