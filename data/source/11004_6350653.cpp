#include <algorithm>
#include <iostream>
using namespace std;
int n,k,ar[5000001];
int main()
{
	cin>>n>>k;
	for(int x=0; x<n; x++)scanf("%d",&ar[x]);
	sort(ar,ar+n);
	cout<<ar[k-1];
}