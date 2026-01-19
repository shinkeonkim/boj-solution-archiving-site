#include <iostream>
#include <string>
using namespace std;
string a;
int A,B;
int main()
{
	cin>>a;
	for(int x=0; x<a.length(); x++)
	{
		if(a[x]=='_') A=1;
		if('A'<=a[x]&&a[x]<='Z') B=1;
	}
	if(A==0&&B==0) A=1;
	
	for(int x=1; x<a.length(); x++)
	{
		if(a[x-1]=='_'&&a[x]=='_')
		{
			cout<<"Error!";
			return 0;
		}
	}
	
	
	if((A==1&&B==1)||('A'<=a[0]&&a[0]<='Z')||a[a.length()-1]=='_'||a[0]=='_')
	{
		cout<<"Error!";
		return 0;
	}
	if(A==1)
	{
		for(int x=0; x<a.length(); x++)
		{
			if(a[x]=='_')
			{
				cout<<(char)(a[x+1]-32);
				x++;
			}
			else cout<<a[x];
		}
	}
	else if(B==1)
	{
		for(int x=0; x<a.length(); x++)
		{
			if('A'<=a[x]&&a[x]<='Z')
			{
				cout<<"_"<<(char)(a[x]+32);
			}
			else cout<<a[x];
		}
	}
}