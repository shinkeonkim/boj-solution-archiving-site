#include <iostream>
#include <string>
#define Mx 9999999
using namespace std;
int N,D[1100];
string a;
int main()
{
	cin>>N;
	cin>>a;
	for(int x=0; x<N; x++)
	{
		D[x]=Mx;
	}
	D[0]=0;
	for(int x=1; x<N; x++)
	{
		for(int y=0; y<x; y++)
		{
			if(a[y]=='J'&&a[x]=='B')
			{
				if(D[y]+(y-x)*(y-x)<D[x])D[x]=D[y]+(y-x)*(y-x);
			}
			else if(a[y]=='B'&&a[x]=='O')
			{
				if(D[y]+(y-x)*(y-x)<D[x])D[x]=D[y]+(y-x)*(y-x);
			}
			else if(a[y]=='O'&&a[x]=='J')
			{
				if(D[y]+(y-x)*(y-x)<D[x])D[x]=D[y]+(y-x)*(y-x);
			}
		}
	}
	if(D[N-1]!=Mx)cout<<D[N-1];
	else cout<<-1;
}