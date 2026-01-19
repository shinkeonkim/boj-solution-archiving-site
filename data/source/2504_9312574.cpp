#include <iostream>
#include <string>
#include <stack>
using namespace std;
string a;
stack <char> stk;
int Cnta,Cntb;
int ar[110];
int main()
{
	cin>>a;
	while(!stk.empty()) stk.pop();
	
	for(int x=0; x<a.length(); x++)
	{
		//if(!stk.empty()) cout<<stk.top();
		if(!stk.empty())
		{
			if(stk.top()=='('&&a[x]==')')
			{
				stk.pop();
			}
			else if(stk.top()=='['&&a[x]==']')
			{
				stk.pop();
			}
			else
			{
				stk.push(a[x]);
			}
		}
		else stk.push(a[x]);
	}
	
	if(!stk.empty()) 
	{
		/*while(!stk.empty())
		{
			cout<<stk.top();
			stk.pop();
		}*/
		cout<<"0";
		return 0;
	}
	
	for(int x=0; x<a.length(); x++)
	{
		if(a[x]=='(') ar[x]=-1;
		if(a[x]==')') ar[x]=-2;
		if(a[x]=='[') ar[x]=-3;
		if(a[x]==']') ar[x]=-4;
	}
	int Cnt=a.length();
	while(Cnt!=1)
	{
		for(int x=0; x<Cnt; x++)
		{
			if(ar[x]==-1)
			{
				if(ar[x+1]==-2)
				{
					ar[x]=2;
					for(int y=x+2; y<Cnt; y++)
					{
						ar[y-1]=ar[y];
					}
					Cnt--;
				}
				if(x+2<Cnt&&ar[x+2]==-2&&ar[x+1]>0)
				{
					ar[x]=ar[x+1]*2;
					for(int y=x+3; y<Cnt; y++)
					{
						ar[y-2]=ar[y];
					}
					Cnt-=2;
				}
			}
			else if(ar[x]==-3)
			{
				if(ar[x+1]==-4)
				{
					ar[x]=3;
					for(int y=x+2; y<Cnt; y++)
					{
						ar[y-1]=ar[y];
					}
					Cnt--;
				}
				
				if(x+2<Cnt&&ar[x+2]==-4&&ar[x+1]>0)
				{
					ar[x]=ar[x+1]*3;
					for(int y=x+3; y<Cnt; y++)
					{
						ar[y-2]=ar[y];
					}
					Cnt-=2;
				}
			}
			else if(ar[x]>0)
			{
				if(ar[x+1]>0&&x+1<Cnt)
				{
					ar[x]=ar[x]+ar[x+1];
					for(int y=x+2; y<Cnt; y++)
					{
						ar[y-1]=ar[y];
					}
					Cnt--;
				}
			}
		}
		//for(int x=0; x<Cnt; x++) cout<<ar[x]<<" ";
		//cout<<endl;
	}
	cout<<ar[0];
}