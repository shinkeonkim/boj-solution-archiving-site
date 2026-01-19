#include <iostream>
#include <cstdio>
using namespace std;
int T,N,ar[1100];
int main()
{
	cin>>T;
	for(int w=0; w<T; w++)
	{
		cin>>N;
		int Sum=0,Cnt=0;
		for(int x=0; x<N; x++)
		{
			cin>>ar[x];
			Sum+=ar[x];
		}
		for(int x=0; x<N; x++)
		{
			if(ar[x]*N>Sum)Cnt++;
		}
		printf("%.3lf%%\n",(double)100*Cnt/N);	
	}
}