#include <iostream>
#include <string>
using namespace std;
string a;
int A,B;
int main()
{
	getline(cin,a);
	for(int x=0; x<a.length()-2; x++)
	{
		if(a[x]==':'&&a[x+1]=='-')
		{
			if(a[x+2]==')') A++;
			if(a[x+2]=='(') B++;
		}
	}
	if(A==0&&B==0) cout<<"none";
	else if(A==B) cout<<"unsure";
	else if(A>B) cout<<"happy";
	else cout<<"sad";
}