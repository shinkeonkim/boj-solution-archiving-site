#include <iostream>
#include <algorithm>
using namespace std;
int n,ar[10005];
long long Sum;
int main()
{
	scanf("%d",&n);
	for(int x=0; x<n; x++) scanf("%d",&ar[x]);
	sort(ar,ar+n);
	for(int x=n-1; x>-1; x--)
	{
		for(int y=0; y<x; y++)
		{
			Sum+=ar[x]-ar[y];
		}
	}
	printf("%lld",Sum*2);
}