#include <iostream>
#include <cstdio> 
using namespace std;
int Q,ar[1100000];
int main()
{
	cin>>Q;
	for(int x=0; x<Q; x++)
	{
		cin>>ar[x];
	}
	for(int x=0; x<Q; x++)
	{
		int S=0;
		while(ar[x]>0)
		{
			S+=ar[x]%2;
			ar[x]/=2;
		}
		if(S==1) printf("1\n");
		else printf("0\n");
	}
} 