#include <iostream>
using namespace std;
long long N,M,ar[1100000],S;
long long a=0,b=1000000000,mid;
int main()
{
	cin>>N>>M;
	for(int x=0; x<N; x++) cin>>ar[x];
	while(a<b)
	{
		S=0;
		mid=(a+b)/2;
		for(int x=0; x<N; x++)
		{
			if(ar[x]>mid) S+=ar[x]-mid;
		}
		
		if(S<M)
		{
			b=mid-1;
		}
		else if(S>M)
		{
			a=mid+1;
		}
		else if(S==M)
		{
			cout<<mid;
			return 0;
		}
	}
	S=0;
	while(1)
	{
		S=0;
		for(int x=0; x<N; x++)
		{
			if(ar[x]>a) S+=ar[x]-a;
		}
		if(S>=M)
		{
			cout<<a;
			return 0;
		}
		else a--;
	}
	
	
}