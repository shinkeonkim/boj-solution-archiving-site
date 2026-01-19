#include <iostream>
using namespace std;
int main()
{
	int a,b,c;
	scanf("%d %d %d",&a,&b,&c);
	b+=c;
	if(b>59)
	{
		a+=b/60;
		b=b%60;
	}
	if(a>23)
	{
		a=a%24;
	}
	printf("%d %d",a,b);
}