#include <iostream>
#include <string>
using namespace std;
string a;
int N,S;
int main()
{
	cin>>N>>a;
	for(int x=0; x<a.length(); x++)
	{
		S+=a[x]-'A'+1;
	}
	cout<<S;
}