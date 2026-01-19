#include <iostream>
#include <string>
using namespace std;
int K;
string a;
string b="UCPC";
int main()
{
	getline(cin,a);
	for(int x=0; x<a.length(); x++)
	{
		if(K==4)
		{
			cout<<"I love UCPC";
			return 0;
		}		
		if(a[x]==b[K]) K++;
	}
	if(K==4)
	{
		cout<<"I love UCPC";
		return 0;
	}
	cout<<"I hate UCPC";
}