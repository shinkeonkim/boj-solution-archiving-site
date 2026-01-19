#include <iostream>
#include <algorithm>
using namespace std;
int n,ar[1000100];
int main()
{
	scanf("%d",&n);
	for(int x=0; x<n; x++)
	{
		scanf("%d",&ar[x]);
	}
	sort(ar,ar+n);
	for(int x=0; x<n; x++) printf("%d\n",ar[x]);
}