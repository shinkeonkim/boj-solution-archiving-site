#include <iostream>
#include <string>
using namespace std;
string a;
int main()
{
	cin>>a;
	for(int x=0; x<a.length(); x++)
	{
		if(a[x]-3-'A'<0)
		{
			cout<<(char)(a[x]+'Z'-'A'-2);
		}
		else cout<<(char)(a[x]-3);
	}
}