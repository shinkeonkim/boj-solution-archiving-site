#include <iostream>
#include <string>
using namespace std;
string a,b;
int N;
int main()
{
	cin>>N;
	cin>>a>>b;
	if(N%2==1)
	{
		for(int x=0; x<a.length(); x++)
		{
			if(a[x]=='0') a[x]='1';
			else a[x]='0';
		}
	}
	if(a==b) cout<<"Deletion succeeded";
	else cout<<"Deletion failed";
}