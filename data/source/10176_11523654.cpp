#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
string a;
int check[33];
int N,K;
char f(char x)
{
	if(x<='M')
	{
		return 'N'+'M'-x;
	}
	else
	{
		return 'M'-(x-'N');
	}
}

int main()
{
	cin>>N;
	for(int x=0; x<N; x++)
	{
		K=0;
		cin>>a;
		for(int x=0; x<a.length(); x++) check[x]=0;
		transform(a.begin(),a.end(),a.begin(),::toupper);
		
		for(int x=0; x<a.length(); x++)
		{
			if('A'<=a[x]&&a[x]<='Z')
			{
				int C=0;
				for(int y=0; y<a.length(); y++)
				{
					if('A'<=a[y]&&a[y]<='Z'&&check[y]==0&&a[y]==f(a[x]))
					{
						check[y]=1;
						C=1;
					}
				}
				if(C==0)
				{
					cout<<"No\n";
					K=1;
					break;
				}
			}
		}
		if(K==0) cout<<"Yes\n";
	}
}