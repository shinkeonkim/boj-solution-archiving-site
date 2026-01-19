#include <iostream>
using namespace std;
int main()
{
	int X,Y,Q,P,A;
	double Z,Min=9999999;
	scanf("%d %d",&X,&Y);
	Z=(double)(X*1000)/Y;
	if(Z<Min)Min=Z;
	scanf("%d",&A);
	for(int x=0; x<A; x++)
	{
		scanf("%d %d",&P,&Q);
		Z=(double)(P*1000)/Q;
		if(Z<Min)Min=Z;
	}
	printf("%.2lf",Min);
}