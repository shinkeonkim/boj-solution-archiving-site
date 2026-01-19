#include <iostream>
#include <string>
#include <stack>
using namespace std;
int T;
stack <char> L,R;
string ar[1100000];
int main()
{
	cin>>T;
	for(int x=0; x<T; x++) cin>>ar[x];
	for(int x=0; x<T; x++)
	{
		
		string A=ar[x];
		
		for(int x=0; x<A.length(); x++)
		{
			if(A[x]=='<')
			{
				if(!L.empty())
				{
					R.push(L.top());
					L.pop();
				}
			}
			else if(A[x]=='>')
			{
				if(!R.empty())
				{
					L.push(R.top());
					R.pop();
				}
			}
			else if(A[x]=='-')
			{
				if(!L.empty())L.pop();
			}
			else
			{
				L.push(A[x]);
			}
		}
		
		while(!L.empty())
		{
			R.push(L.top());
			L.pop();
		}
		while(!R.empty())
		{
			cout<<R.top();
			R.pop();
		}
		cout<<endl;
		
	}
}