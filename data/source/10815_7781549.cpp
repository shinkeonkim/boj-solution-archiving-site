#include <iostream>
#include <algorithm>
using namespace std;
int N,ar[550000],N2,Q[550000],check[550000];
int Find(int left,int right,int x)
{
	if(left>right) return 0;
	else if(left==right&&ar[left]==x) return 1;
	else if(left==right) return 0;
	else
	{
		int mid;
		mid=(left+right)/2;
		if(ar[mid]==x) return 1;
		else if(ar[mid]<x) return Find(mid+1,right,x);
		else return Find(left,mid,x);
	}
}
int main()
{
	cin>>N;
	for(int x=0; x<N; x++) cin>>ar[x];
	cin>>N2;
	for(int x=0; x<N2; x++) cin>>Q[x];
	sort(ar,ar+N);
	for(int x=0; x<N2; x++)
	{
		check[x]=Find(0,N-1,Q[x]);
	}
	for(int x=0; x<N2; x++) cout<<check[x]<<" ";
}