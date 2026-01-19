#include <iostream>
using namespace std;
int N,Max,A,B,C;
int f(int a,int b,int c)
{ 
	if(a==b&&b==c)
	{
		return 10000+a*1000;
	}
	else if(a==b||b==c)
	{
		return 1000+b*100;
	}
	else if(a==c)
	{
		return 1000+a*100;
	}
	else
	{
		if(a>=b&&a>=c) return a*100;
		if(b>=c&&b>=a) return b*100;
		if(c>=a&&c>=b) return c*100;
	}
}
int main()
{
	cin>>N;
	for(int x=0; x<N; x++)
	{
		cin>>A>>B>>C;
		if(f(A,B,C)>Max) Max=f(A,B,C);
	}
	cout<<Max;
} 