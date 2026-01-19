#include <string>
#include <iostream>
using namespace std;
string a,b,c;
char A;
int main()
{
	cin>>a>>A>>b;
	if(A=='+')
	{
		if(a.length()==b.length())
		{
			cout<<"2";
			for(int x=1; x<a.length(); x++)cout<<"0";
		}
		else
		{
			if(a.length()<b.length())
			{
				c=a;
				a=b;
				b=c;
			}
			cout<<"1";
			for(int x=1; x<a.length(); x++)
			{
				if(a.length()-b.length()==x) cout<<"1";
				else cout<<"0";
			}
			
		}
	}
	else if(A=='*')
	{
		cout<<"1";
		for(int x=0; x<a.length()+b.length()-2; x++) cout<<"0";
	}
}