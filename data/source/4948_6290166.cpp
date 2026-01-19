#include <iostream>
using namespace std;
int ar[250000],n=1;
int main()
{
	for(int y=2; y<250000; y++) ar[y]=y;
	for(int y=2; y<250000; y++)
	{
		if(ar[y]==y)
		{
			for(int z=y+y; z<250000; z+=y)ar[z]=0;
		}
	}
	while(n!=0)
	{
		int Cnt=0;
		cin>>n;
		if(n!=0)
		{
			for(int x=n+1; x<2*n+1; x++)
		{
			if(ar[x]==x)Cnt++;
		}
		cout<<Cnt<<endl;
		}
	}
}