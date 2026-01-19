#include <iostream>
using namespace std;
long long A,B;

long long f(long long a,long long b)
{
	return b>0?f(b,a%b):a;
}

int main()
{
	cin>>A>>B;
	for(int x=0; x<f(A,B); x++) cout<<1;
}