#include <iostream>
using namespace std;
long long A,B;
int T;
long long f(long long a,long long b)
{
	return b>0?f(b,a%b):a;
}
int main()
{
	cin>>T;
	for(int x=0; x<T; x++)
	{
		cin>>A>>B;
		cout<<A/f(A,B)*B<<endl;
	}
}