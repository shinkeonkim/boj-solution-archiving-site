#include <iostream>
#include <string>
using namespace std;
string a;
int Cnt;
int main()
{
	cin>>a;
	for(int x=0; x<a.length(); x++)
	{
		if(a[x]=='c')
		{
			if(a[x+1]=='=')
			{
				x++;
				Cnt++;
			}
			else if(a[x+1]=='-')
			{
				x++;
				Cnt++;
			}
			else
			{
				Cnt++;
			}
		}
		else if(a[x]=='d')
		{
			if(a[x+1]=='z'&&a[x+2]=='=')
			{
				x+=2;
				Cnt++;
			}
			else if(a[x+1]=='-')
			{
				x++;
				Cnt++;
			}
			else
			{
				Cnt++;
			}
		}
		else if(a[x]=='l'&&a[x+1]=='j')
		{
			x++;
			Cnt++;
		}
		else if(a[x]=='n'&&a[x+1]=='j')
		{
			x++;
			Cnt++;
		}
		else if(a[x]=='s'&&a[x+1]=='=')
		{
			x++;
			Cnt++;
		}
		else if(a[x]=='z'&&a[x+1]=='=')
		{
			x++;
			Cnt++;
		}
		else
		{
			Cnt++;
		}
	}
	cout<<Cnt;
}