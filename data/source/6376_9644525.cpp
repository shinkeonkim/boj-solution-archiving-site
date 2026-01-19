#include <iostream>
#include <cstdio>
using namespace std;
double a,n=2.0,k=1;
int main()
{
	printf("n e\n- -----------\n");
	printf("0 1\n1 2\n");
	for(int x=2; x<10; x++)
	{
		cout<<x<<" ";
		k*=x;
		n+=(double)1/k;
		if(x>=3) printf("%.9lf\n",n);
		else printf("%.1lf\n",n);
	}
}