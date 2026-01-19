#include <iostream>
int main()
{
	int a,b,Min=10001,Sum=0;
	scanf("%d %d",&a,&b);
	for(int x=100; x>0; x--)
	{
		if(x*x>=a&&x*x<=b)
		{
			if(Min>x*x) Min=x*x;
			Sum+=x*x;
		}
	}
	if(Min==10001) printf("-1");
	else printf("%d\n%d",Sum,Min);
}