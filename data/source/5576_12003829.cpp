#include <iostream>
#include <algorithm>
using namespace std;
int A,B,a[11],b[11];
int main()
{
	for(int x=0; x<10; x++)
	{
		cin>>a[x];
	}
	sort(a,a+10);
	for(int x=0; x<10; x++)
	{
		cin>>b[x];
	}
	sort(b,b+10);
	for(int x=7; x<10; x++)
	{
		A+=a[x];
		B+=b[x];
	}
	cout<<A<<" "<<B;
}