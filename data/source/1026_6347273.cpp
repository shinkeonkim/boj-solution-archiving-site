#include <iostream>
#include <algorithm>
using namespace std;
int n,ar1[53],ar2[53],Sum;
int main()
{
	cin>>n;
	for(int x=0; x<n; x++)cin>>ar1[x];
	for(int x=0; x<n; x++)cin>>ar2[x];
	
	sort(ar1,ar1+n);
	sort(ar2,ar2+n);
	for(int x=0; x<n; x++)
	{
		Sum+=ar1[x]*ar2[n-1-x];
	}
	cout<<Sum;
}