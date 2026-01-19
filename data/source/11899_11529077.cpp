#include <iostream>
#include <stack>
#include <string>
using namespace std;

stack <char> S;
string a;
int Cnt;
int main()
{
	cin>>a;
	for(int x=0; x<a.length(); x++)
	{
		if(a[x]=='(') S.push(a[x]);
		else if(a[x]==')')
		{
			if(S.empty()) Cnt++;
			else S.pop();
		}
	}
	cout<<Cnt+S.size();
}