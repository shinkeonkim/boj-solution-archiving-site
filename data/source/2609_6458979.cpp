#include <iostream>
using namespace std;
int main()
{
	int a,b,memo;
	scanf("%d %d",&a,&b);
	if(a>b)
	{
		int tmp;
		tmp=b;
		b=a;
		a=tmp;
	}
	for(int x=1; x<=b; x++)
	{
		if(a%x==0&&b%x==0) memo=x;
	}
	printf("%d\n%d",memo,(a*b)/memo);
}