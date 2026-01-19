#include <iostream>
using namespace std;
int check[33],a;
int main()
{
	for(int x=0; x<28; x++)
	{
		cin>>a;
		check[a]=1;
	}
	for(int x=1; x<=30; x++)
	{
		if(check[x]==0) cout<<x<<endl;
	}
}