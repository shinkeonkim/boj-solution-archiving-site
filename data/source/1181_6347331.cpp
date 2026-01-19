#include <iostream>
#include <algorithm>
#include <string.h>
using namespace std;
struct Baam
{
	int l;
	char aaa[55];
};
int Compare(Baam a,Baam b)
{
	if(a.l<b.l) return true;
	if(a.l==b.l)
	{
		if(strcmp(a.aaa,b.aaa)<0) return true;
	}
	return false;
}
int main()
{
	int n;
	Baam ar[20005];
	cin>>n;
	for(int x=0; x<n; x++)
	{
		scanf("%s",ar[x].aaa);
		ar[x].l=strlen(ar[x].aaa);
	}
	sort(ar,ar+n,Compare);
	for(int x=0; x<n-1; x++)
	{
		if(strcmp(ar[x].aaa,ar[x+1].aaa)==0) ar[x].aaa[0]=0;
	}
	for(int x=0; x<n; x++)
	{
		if(ar[x].aaa[0]!=0)printf("%s\n",ar[x].aaa);
	}
	
}