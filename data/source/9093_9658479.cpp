#include <iostream>
#include <cstdio>
#include <stack>
#include <cstring>
using namespace std;

char ar[2200];
int N;
stack <char> stk;

int main()
{
	cin>>N;
	scanf("\n");
	for(int q=0; q<N; q++)
	{
		fgets(ar,1100,stdin);
		for(int y=0; y<strlen(ar); y++)
		{
			if(ar[y]==' ')
			{	
				while(!stk.empty())
				{
					cout<<stk.top();
					stk.pop();
				}
				cout<<" ";
			}
			else if(ar[y]!='\n')stk.push(ar[y]);
		}
		while(!stk.empty())
		{	
			cout<<stk.top();
			stk.pop();
		}
		cout<<"\n";
	}
	
}