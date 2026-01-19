#include <iostream>
using namespace std;
int main()
{
	int Flag,Max=0;
	for(int x=1; x<=5; x++)
	{
		int Sum=0;
		for(int y=0; y<4; y++)
		{
			int a;
			scanf("%d",&a);
			Sum+=a;
		}
		if(Max<Sum)
		{
			Max=Sum;
			Flag=x;
		}
	}
	printf("%d %d",Flag,Max);
}