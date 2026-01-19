#include <iostream>
using namespace std;
char ar[20][20];
int main()
{
	for(int x=0; x<5; x++)cin>>ar[x];
	for(int x=0; x<15; x++)
	{
		for(int y=0; y<5; y++)
		{
			if(ar[y][x]!=0)cout<<ar[y][x];
		}
	}
} 