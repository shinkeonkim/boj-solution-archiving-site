#include <iostream>
using namespace std;
int ar[10010];
int main()
{
	for(int x=1; x<=10000000; x++)
	{
		int Sum=x;
		int y=x;
		while(y>0)
		{
			Sum+=y%10;
			y/=10;
		}
		if(Sum<10001)ar[Sum]=1;
	}
	for(int x=1; x<10001; x++)
	{
		if(ar[x]==0) printf("%d\n",x);
	}
}