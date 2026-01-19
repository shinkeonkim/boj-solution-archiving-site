#include <iostream>
#include <cstdio>
using namespace std;
int T,ar[20];
int main()
{
	cin>>T;
	for(int w=0; w<T; w++)
	{
		int Sum=0;
		for(int x=0; x<16; x++)
		{
			scanf("%1d",&ar[x]);
		}
		for(int x=0; x<16; x++)
		{
			if(x%2==0)
			{
				ar[x]*=2;
				if(ar[x]>9)
				{
					ar[x]=(ar[x]/10)+(ar[x]%10);
				}
			}
			//cout<<ar[x]<<" ";
			Sum+=ar[x];
		}
		
		if(Sum%10==0) cout<<"T\n";
		else cout<<"F\n";
	}
}