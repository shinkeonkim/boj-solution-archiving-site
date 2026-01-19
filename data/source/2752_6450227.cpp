#include <iostream>
#include <algorithm>
using namespace std;
int n,ar[5];
int main()
{
	n=3;
	for(int x=0; x<n; x++)
	{
		scanf("%d",&ar[x]);
	}
	sort(ar,ar+n);
	for(int x=0; x<n; x++) printf("%d ",ar[x]);
}