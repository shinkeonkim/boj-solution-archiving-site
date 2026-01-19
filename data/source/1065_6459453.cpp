#include <iostream>
using namespace std;
int a,Cnt;
int main()
{
	scanf("%d",&a);
	for(int x=1; x<=a; x++)
	{
		int flag=0;
		int z=x;
		if(z<100) Cnt++;
		else
		{
			int gap=0;
			int y1=z%10;
			z/=10;
			int y2=z%10;
			z/=10;
			gap=y1-y2;
			y1=y2;
			while(z>0)
			{
				y2=z%10;
				z/=10;
				if(gap!=y1-y2) flag=1;
				y1=y2;
			}
			if(flag==0)Cnt++;
		}
	}
	printf("%d",Cnt);
}