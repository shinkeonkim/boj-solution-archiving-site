#include <iostream>
using namespace std;
struct st{
	int a;
	char b;
};
int K,N,T;

st ar[110];

int main()
{
	cin>>K>>N;
	for(int x=0; x<N; x++)
	{
		cin>>ar[x].a>>ar[x].b;	
	}
	for(int x=0; x<N; x++)
	{
		T+=ar[x].a;
		if(T>=210)
		{
			if(K%8==0) cout<<8;
			else cout<<K%8;
			return 0;
		}
		else
		{
			if(ar[x].b=='T') K++;
		}
	}
}