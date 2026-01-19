#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
string a;
int ar[110000],N;

bool compare(int a,int b)
{
	if(a>b) return true;
	return false;
}

int main()
{
	cin>>a;
	for(int x=0; x<a.length(); x++) ar[x]=a[x]-48;
	N=a.length();
	sort(ar,ar+N,compare);
	if(ar[N-1]==0)
	{
		int S=0;
		for(int x=0; x<N; x++) S+=ar[x];
		if(S%3==0) 
		{
			for(int x=0; x<N; x++)cout<<ar[x];
		}
		else cout<<-1;
	}
	else
	{
		cout<<-1;	
	}
}