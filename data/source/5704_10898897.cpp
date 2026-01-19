#include <iostream>
#include <string>
using namespace std;
int check[30]; //-97
string a;
string b="*";
int main()
{
	while(1)
	{
		getline(cin,a);
		if(a==b) return 0;
		else
		{
			for(int x=0; x<26; x++) check[x]=0;
			
			for(int x=0; x<a.length(); x++)
			{
				if(a[x]!=' ') check[a[x]-97]=1;
			}
			int C=0;
			for(int x=0; x<26; x++)
			{
				if(check[x]!=1)
				{
					C=1;
					cout<<"N\n";
					break;
				}
			}
			if(!C) cout<<"Y\n";
		}
	}
}