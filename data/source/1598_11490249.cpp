#include <iostream>
using namespace std;
int A,B;
int a,b,c,d;
int f(int x)
{
	return x>0?x:-x;
}
int main()
{
	cin>>A>>B;
	a=A%4;
	b=B%4;
	if(a==0) a=4;
	if(b==0) b=4;
	
	c=A/4;
	if(A%4==0) c--;
	
	d=B/4;
	if(B%4==0) d--;
	
	cout<<f(a-b)+f(c-d);
}