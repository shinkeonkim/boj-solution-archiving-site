#include <iostream>
#include <string>
#include <algorithm>
#include <stack>
using namespace std;
string a;
string ar[4400];
int archeck[4400],check[20],Cnt=1,arCnt;
stack <int> stk;

bool test()
{
	for(int x=0; x<a.length()-1; x++)
	{
		if(a[x]==')'&&a[x+1]=='(')
		{
			if(check[archeck[x]]==0&&check[archeck[x+1]]==0) return true;
		}
		if(x>0&&a[x]=='('&&'0'<=a[x-1]&&a[x-1]<='9'&&check[archeck[x]]==0) return true;
	}
	return false;
}

void g()
{
	bool flag=true;
	for(int x=1; x<Cnt; x++) if(check[x]==0) flag=false;
	
	if(flag==true) ;
	else if(test()) ;
	else
	{
		for(int x=0; x<a.length(); x++)
		{
			if(archeck[x]>0&&check[archeck[x]]==1)
			{
				ar[arCnt].push_back(a[x]);
			}
			else if(archeck[x]==0) ar[arCnt].push_back(a[x]);
		}
		arCnt++;	
	}
}
int f(int X)
{
	if(X<Cnt-1)
	{
		for(int x=0; x<2; x++)
		{
			check[X]=x;
			f(X+1);
		}
	}
	else if(X==Cnt-1)
	{
		for(int x=0; x<2; x++)
		{
			check[X]=x;
			g();
		}		
	} 
}
int main()
{
	cin>>a;
	for(int x=0; x<a.length(); x++)
	{
		if(a[x]=='(')
		{
			archeck[x]=Cnt;
			Cnt++;
			stk.push(x);
		}
		else if(a[x]==')')
		{
			archeck[x]=archeck[stk.top()];
			stk.pop();
		}
	}
	for(int x=0; x<2; x++)
	{
		check[0]=x;
		f(1);
	}
	sort(ar,ar+arCnt);
	cout<<ar[0]<<endl;;
	for(int x=1; x<=arCnt; x++)
	{
		if(ar[x]!=ar[x-1]) cout<<ar[x]<<endl;
	}
}