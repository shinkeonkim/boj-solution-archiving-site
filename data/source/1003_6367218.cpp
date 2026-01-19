#include <iostream>
using namespace std;
int ar1[50],ar2[50];
int f1(int x)
{
	if(ar1[x])return ar1[x];
	else if(x==0) return ar1[x]=1;
	else if(x==1) return ar1[x]=0;
	else return ar1[x]=f1(x-1)+f1(x-2);	
}
int f2(int x)
{
	if(ar2[x])return ar2[x];
	else if(x==0) return ar2[x]=0;
	else if(x==1) return ar2[x]=1;
	else return ar2[x]=f2(x-1)+f2(x-2);	
}
int main()
{
	int T;
	scanf("%d",&T);
	for(int x=0; x<T; x++)
	{
		int a;
		scanf("%d",&a);
		printf("%d %d\n",f1(a),f2(a));
	}
}