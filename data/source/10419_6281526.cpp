#include <iostream>
using namespace std;
int n,ar[100],ar2[100];
int main()
{
	cin>>n;
	for(int x=0; x<n; x++) cin>>ar[x];
	for(int x=0; x<n; x++)
	{
		for(int y=0; y<10001; y++)
		{
			if(y*y+y<=ar[x]) ar2[x]=y;
		}
	}
	for(int x=0; x<n; x++)
	{
		cout<<ar2[x]<<endl;
	}
}