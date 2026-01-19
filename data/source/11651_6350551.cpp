#include <algorithm> 
#include <iostream>
using namespace std;
struct xy
{
	int x,y;	
};
int Compare(xy a,xy b)
{
	if(a.y<b.y) return true;
	if(a.y==b.y)
	{
		if(a.x<b.x)return true;
	}
	return false;
}
int main()
{
	xy ar[100001];
	int n;
	cin>>n;
	for(int x=0; x<n; x++)
	{
		scanf("%d %d",&ar[x].x,&ar[x].y);
	}
	sort(ar,ar+n,Compare);
	for(int x=0; x<n; x++)
	{
		printf("%d %d\n",ar[x].x,ar[x].y);
	}
}