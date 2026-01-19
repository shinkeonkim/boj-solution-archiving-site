#include <iostream>
#include <string>
using namespace std;
int A,B;
string a[11];
int main()
{
	cin>>A>>B;
	for(int x=0; x<A; x++)
	{
		cin>>a[x];
	}
	for(int x=0; x<A; x++)
	{
		for(int y=B-1; y>-1; y--)
		{
			cout<<a[x][y];
		}
		cout<<endl;
	}
}