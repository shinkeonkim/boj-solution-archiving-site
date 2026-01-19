#include <iostream>
using namespace std;
int N,Max=0;
bool f(int x)
{
	int A=x;
	while(A>0)
	{
		if(A%10==4||A%10==7) ;
		else return false;
		A/=10;
	}
	return true;
}
int main()
{
	cin>>N;
	for(int x=1; x<=N; x++)
	{
		if(f(x))
		{
			if(Max<x) Max=x;
		}
	}
	cout<<Max;
} 