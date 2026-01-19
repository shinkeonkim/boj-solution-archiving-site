#include <iostream>
using namespace std;
int main()
{
	int a,b,c,d;
	scanf("%d %d %d %d",&a,&b,&c,&d);
	c+=d;
	if(c>59)
	{
		b+=c/60;
		c=c%60;
	}
	if(b>59)
	{
		a+=b/60;
		b=b%60;
	}
	if(a>23)
	{
		a=a%24;
	}
	printf("%d %d %d",a,b,c);
}