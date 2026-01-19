#include <iostream>
using namespace std;
string a;
int N;
int f(int x)
{
	if(x<=9) return x;
	else 
	{
		int s=0;
		while(x>0)
		{
			s+=x%10;
			x/=10;
		}
		return f(s);
	}
}
int main()
{
	while(1)
	{
		cin>>a;
		if(a.length()==1&&a[0]=='0') break;
		N=0;
		for(int x=0; x<a.length(); x++)
		{
			N+=a[x]-48;	
		}
		cout<<f(N)<<endl;
	}
}