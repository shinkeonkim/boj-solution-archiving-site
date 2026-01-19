#include <iostream>
#include <algorithm>
using namespace std;
int a[3];
int main()
{
	for(int x=0;x<3;x++)cin>>a[x];
	sort(a,a+3);
	cout<<a[1];
}