#include <iostream>
#include <string>
using namespace std;
string a,b;
int Min=99999,C;
int main()
{
	cin>>a>>b;
	for(int x=0; x<=b.length()-a.length(); x++)
	{
		C=0;
		for(int y=0; y<a.length(); y++)
		{
			if(a[y]!=b[y+x]) C++;
		}
		if(C<Min) Min=C;
	}
	cout<<Min;
}