#include <iostream>
using namespace std;
int ar[30]={1},T;
int main()
{
	cin>>T;
	for(int x=0; x<15; x++)
	{
		ar[x+1]+=ar[x];
		ar[x+2]+=ar[x];
		ar[x+3]+=ar[x];
	}
	for(int x=0; x<T; x++)
	{
		int a;
		cin>>a;
		cout<<ar[a]<<endl;
	}
}