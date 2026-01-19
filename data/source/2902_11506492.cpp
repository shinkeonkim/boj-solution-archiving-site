#include <iostream>
#include <string>
using namespace std;
string a;
int main()
{
	cin>>a;
	for(int x=0; x<a.length(); x++)
	{
		if(65<=a[x]&&a[x]<=90) cout<<a[x];	
	}	
}