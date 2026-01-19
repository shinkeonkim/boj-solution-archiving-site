#include<iostream>
using namespace std;
int ar[42],Cnt;
int main()
{
	for(int x=0; x<10; x++)
	{
		int a;
		scanf("%d",&a);
		ar[a%42]++;
	}
	for(int x=0; x<42; x++)
	{
		if(ar[x]>0)Cnt++;
	}printf("%d",Cnt);
}