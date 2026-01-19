#include <iostream>
using namespace std;
int n,z=2;
int main()
{
	scanf("%d",&n);
	if(n==1) ;
	else
	{
		while(n>1)
		{
			while(n%z==0)
			{
				printf("%d\n",z);
				n/=z;
			}
		z++;
		}
	}
	
}