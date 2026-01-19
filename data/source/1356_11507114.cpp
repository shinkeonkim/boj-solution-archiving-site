#include <iostream>
#include <string>
using namespace std;
string a;
int ar[22],A,B,C,D;
int main()
{
	cin>>a;
	for(int x=0; x<a.length(); x++) ar[x]=a[x]-'0';
	for(int x=0; x<a.length(); x++)
	{
		A=B=1;
		C=D=0;
		
		for(int y=0; y<=x; y++) 
		{
			C=1;
			A*=ar[y];
		}
		for(int z=x+1; z<a.length(); z++) 
		{
			D=1;
			B*=ar[z];
		}
		if(C&&D&&A==B)
		{
			cout<<"YES";
			return 0;
		}
	}
	cout<<"NO";
}
