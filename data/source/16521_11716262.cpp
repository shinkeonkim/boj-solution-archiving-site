#include <iostream>
#include <cstdio>
using namespace std;
long long A,B,A1,A2;
long long f(long long x, long long y)
{
	return y>0?f(y,x%y):x;
}
int main()
{
	scanf("%lld.%lld",&A1,&A2);
	B=36000;
	A=A1*100+A2;
	cout<<36000/f(A,B);
}