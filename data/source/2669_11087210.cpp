#include <iostream>
using namespace std;
int x1,y1,x2,y2,Cnt;
int ar[110][110];
int main()
{
	for(int d=0; d<4; d++)
	{
		cin>>x1>>y1>>x2>>y2;
		for(int X=x1; X<x2; X++)
		{
			for(int Y=y1; Y<y2; Y++)
			{
				ar[X][Y]=1;
			}
		}
	}
	
	for(int x=1; x<=100; x++)
	{
		for(int y=1; y<=100; y++) Cnt+=ar[x][y];
	}
	cout<<Cnt;
}