#include <iostream>
#include <cstdio>
using namespace std;
int ar[1000000],m,n;
int main()
{
	cin>>m>>n;
	for(int y=2; y<1000001; y++) ar[y]=y;
	for(int y=2; y<n; y++)
	{
		if(ar[y]==y)
		{
			for(int z=y+y; z<=n; z+=y)ar[z]=0;
		}
	}
	for(int z=m; z<=n; z++)
	{
		if(ar[z]==z) 
        {
            printf("%d\n",z);
        }
	} 
}