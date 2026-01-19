#include <iostream>
#include <string>
using namespace std;
string a;
int main()
{
	cin>>a;
	for(int x=0; x<a.length(); x++)
	{
		if(x!=0&&x%10==0)cout<<endl;
		cout<<a[x];
	}
}