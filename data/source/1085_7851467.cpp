#include<iostream>
#define Min(a,b) (a>b?b:a)
using namespace std;
int a,b,c,d;
int main()
{
	cin>>a>>b>>c>>d;
	a=Min(a,c-a);
	b=Min(b,d-b);
	cout<<Min(a,b);
}