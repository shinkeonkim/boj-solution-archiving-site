#include <iostream>
using namespace std;
int N,K,ar[1100],Cnt,Flag,check;
int main()
{
	cin>>N>>K;
	for(int x=2; x<=N; x++) ar[x]=x;
	for(int x=2; x<=N; x++)
	{
		if(ar[x])
		{
			for(int y=x; y<=N; y+=x)
			{
				if(ar[y]) Cnt++;
				if(Cnt==K) 
				{
					Flag=y,check=1;
					break;
				}
				ar[y]=0;
				
			}
		}
		if(check) break;
	}
	cout<<Flag;
}