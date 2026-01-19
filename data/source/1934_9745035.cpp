#include <iostream>
using namespace std;
int T,a[1100],b[1100];
int gcd(int a,int b)
{
	return b?gcd(b,a%b):a;
}
int main()
{
	cin>>T;
	for(int x=0; x<T; x++)cin>>a[x]>>b[x];
	for(int x=0; x<T; x++)
	{
		cout<<a[x]*b[x]/gcd(a[x],b[x])<<endl;
	}
}