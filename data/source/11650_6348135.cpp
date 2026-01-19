#include <algorithm> 
#include <iostream>
using namespace std;
struct xy
{
	int x,y;	
};
int Compare(xy a,xy b)
{
	if(a.x<b.x) return true;
	if(a.x==b.x)
	{
		if(a.y<b.y)return true;
	}
	return false;
}
int main()
{
	xy ar[100001];
	int n;
	scanf("%d",&n);
	for(int x=0; x<n; x++)
	{
		scanf("%d",&ar[x].x);
		scanf("%d",&ar[x].y);
	}
	sort(ar,ar+n,Compare);
	for(int x=0; x<n; x++)
	{
		printf("%d ",ar[x].x);
		printf("%d \n",ar[x].y);
	}
}