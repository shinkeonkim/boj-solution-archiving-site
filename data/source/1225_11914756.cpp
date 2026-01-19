#include <iostream>
#include <string>
using namespace std;
long long A,B;
string a,b; 
int main()
{
	cin>>a>>b;
	for(int x=0; x<a.length(); x++)
	{
		A+=a[x]-'0';
	}
	for(int x=0; x<b.length(); x++)
	{
		B+=b[x]-'0';
	}
	cout<<A*B;
}