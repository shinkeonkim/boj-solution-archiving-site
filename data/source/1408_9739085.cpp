#include <iostream>
#include <cstdio>
using namespace std;
int a,b,c,A,B,T;
int main()
{
	scanf("%d:%d:%d",&a,&b,&c);
	A=a*3600+b*60+c;
	scanf("%d:%d:%d",&a,&b,&c);
	B=a*3600+b*60+c;
	if(A>B)
	{
		T=3600*24-(A-B);
		printf("%02d:",T/3600);
		T%=3600;
		printf("%02d:",T/60);
		T%=60;
		printf("%02d",T);
	}else
	{
		T=B-A;
		printf("%02d:",T/3600);
		T%=3600;
		printf("%02d:",T/60);
		T%=60;
		printf("%02d",T);
	}
}