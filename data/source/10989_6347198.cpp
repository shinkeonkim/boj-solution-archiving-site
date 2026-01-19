#include <iostream>
#include <algorithm>
#include <stdio.h>
using namespace std;
int ar[10001],n;
int main()
{
	scanf("%d",&n);
	for(int x=0; x<n; x++)
	{
		int a;
		scanf("%d",&a);
		ar[a]++;
		
	}
	for(int x=0; x<10001; x++)
	{
		if(ar[x]>0)
		{
			for(int y=0;y<ar[x]; y++)
			{
				printf("%d\n",x);	
			}	
		}	
	}
	return 0;
}