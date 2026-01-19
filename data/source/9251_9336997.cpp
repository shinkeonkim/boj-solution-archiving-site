#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
string a,b;
int ar[1100][1100],Max;
int main()
{
	cin>>a>>b;
	for(int x=1; x<=a.length(); x++)
	{
		for(int y=1; y<=b.length(); y++)
		{
			if(a[x-1]==b[y-1])
			{
				ar[x][y]=1+ar[x-1][y-1];
			}
			else if(ar[x-1][y]>=ar[x][y-1])
			{
				ar[x][y]=ar[x-1][y];
			}
			else ar[x][y]=ar[x][y-1];
			Max=max(Max,ar[x][y]);
		}
	}
	cout<<Max;
}