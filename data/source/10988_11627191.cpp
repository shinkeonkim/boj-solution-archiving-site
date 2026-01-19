#include <iostream>
#include <string>
using namespace std;
string a;
int main()
{
	cin>>a;
	for(int x=0; x<a.length(); x++)
	{
		if(a[x]!=a[a.length()-x-1])
		{
			cout<<0;
			return 0;
		}
	}
	cout<<1;
}