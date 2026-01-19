#include<iostream>
using namespace std;
int main()
{
	int P,Cnt=0;
	scanf("%d",&P);
	P=1000-P;
	while(P>499)
	{
		Cnt++;
		P-=500;
	}
	while(P>99)
	{
		Cnt++;
		P-=100;
	}
	while(P>49)
	{
		Cnt++;
		P-=50;
	}
	while(P>9)
	{
		Cnt++;
		P-=10;
	}
	while(P>4)
	{
		Cnt++;
		P-=5;
	}
	while(P>0)
	{
		Cnt++;
		P-=1;
	}
	printf("%d",Cnt);
}

