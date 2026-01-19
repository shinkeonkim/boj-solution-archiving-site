#include <iostream>
using namespace std;
int a,b,c,d,z,q,S,X;
int gcd(int x,int y)
{
	return y?gcd(y,x%y):x;
}
int main()
{
	cin>>a>>b>>c>>d;
	q=gcd(b,d);
	z=(b*d)/q;
	S+=(z/b)*a+(z/d)*c;
	X=gcd(S,z);
	cout<<S/X<<" "<<z/X;
}