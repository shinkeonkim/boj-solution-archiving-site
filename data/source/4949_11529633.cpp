#include <iostream>
#include <stack>
using namespace std;
stack <char> S;
string a;
string b=".";
bool check;
int main()
{
	while(1)
	{
		check=true;
		getline(cin,a);
		if(a==b) return 0;
		for(int x=0; x<a.length(); x++)
		{
			if(a[x]=='('||a[x]=='[') S.push(a[x]);
			else if(a[x]==')')
			{
				if(S.empty())
				{
					check=false;
					break;
				}
				else if(S.top()=='[')
				{
					check=false;
				}
				else S.pop();
			}
			else if(a[x]==']')
			{
				if(S.empty())
				{
					check=false;
					break;
				}
				else if(S.top()=='(')
				{
					check=false;
				}
				else S.pop();
			}
		}
		if(!S.empty()) check=false;
		while(!S.empty()) S.pop();
		if(check) cout<<"yes\n";
		else cout<<"no\n";
	}
}