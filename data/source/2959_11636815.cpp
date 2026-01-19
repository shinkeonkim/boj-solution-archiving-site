#include <iostream>
#include <algorithm>
using namespace std;
int a[5];
int main()
{
	for(int x=0; x<4; x++) cin>>a[x];
	sort(a,a+4);
	cout<<a[0]*a[2];
}