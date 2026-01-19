#include <iostream>
#include <algorithm>
using namespace std;
int n,ar[100100];
int main()
{
	scanf("%d",&n);
	for(int x=0; x<n; x++)
	{
		scanf("%d",&ar[x]);
	}
	sort(ar,ar+n);
	printf("%d ",ar[0]);
	for(int x=1; x<n; x++)
	{
		if(ar[x]!=ar[x-1]) printf("%d ",ar[x]);
	}
}