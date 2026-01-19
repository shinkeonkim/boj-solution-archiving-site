#include <iostream>
using namespace std;
char ar[10][10];
int Cnt;
int main()
{
	for(int y=0; y<8; y++)scanf("%s",ar[y]);
	for(int y=0; y<8; y++)
	{
		for(int x=0; x<8; x++)
		{
			if(y%2==0)
			{
				if(x%2==0&&ar[y][x]=='F')Cnt++;
			}
			else
			{
				if(x%2==1&&ar[y][x]=='F')Cnt++;
			}
			
		}
	}
	printf("%d",Cnt);
}