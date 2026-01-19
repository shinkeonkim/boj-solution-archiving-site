#include <iostream>
using namespace std;
int a,b,c; //+ - * /
int main()
{
	cin>>a>>b>>c;
	for(int x=0; x<4; x++)
	{
		if(x==0)
		{
			if(a==b+c)
			{
				cout<<a<<"="<<b<<"+"<<c;
				return 0;
			}
		}
		if(x==1)
		{
			if(a==b-c)
			{
				cout<<a<<"="<<b<<"-"<<c;
				return 0;
			}
		}
		if(x==2)
		{
			if(a==b*c)
			{
				cout<<a<<"="<<b<<"*"<<c;
				return 0;
			}
		}
		if(x==3)
		{
			if(a==b/c&&b%c==0)
			{
				cout<<a<<"="<<b<<"/"<<c;
				return 0;
			}
		}
	}
	for(int x=0; x<4; x++)
	{
		if(x==0)
		{
			if(a+b==c)
			{
				cout<<a<<"+"<<b<<"="<<c;
				return 0;
			}
		}
		if(x==1)
		{
			if(a-b==c)
			{
				cout<<a<<"-"<<b<<"="<<c;
				return 0;
			}
		}
		if(x==2)
		{
			if(a*b==c)
			{
				cout<<a<<"*"<<b<<"="<<c;
				return 0;
			}
		}
		if(x==3)
		{
			if(a/b==c&&a%b==0)
			{
				cout<<a<<"/"<<b<<"="<<c;
				return 0;
			}
		}
	}
}