#include <iostream>
using namespace std;
int ar[10001],m,n,x,Sum,Min;
int main()
{
	cin>>m>>n;
	for(int y=2; y<10001; y++)ar[y]=y;
	for(int y=2; y<10001; y++)
	{
		if(ar[y]==y)
		{
			for(int z=y+y; z<10001; z+=y)ar[z]=0;
		}
	}
	for(int y=n; y>=m; y--)
	{
		if(ar[y]==y) Sum+=y,Min=y;
	}
	if(Sum>0)cout<<Sum<<endl<<Min;
	else cout<<-1; 
}