#include <iostream>
using namespace std;
long long A,B;
long long f(long long x, long long y)
{
	return y>0?f(y,x%y):x;
}
int main()
{
	cin>>A>>B;
	cout<<(A/f(A,B))*B;
}