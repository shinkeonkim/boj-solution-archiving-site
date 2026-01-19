#include <iostream>
#define Mx 999999999
using namespace std;
int N,ar[4400000],check[4400000],array;
int main()
{
	cin>>N;
	for(int x=2; x<=N; x++) ar[x]=Mx;
	for(int x=1; x<=N; x++)
	{
		if(ar[x*3]>ar[x]+1)ar[x*3]=ar[x]+1,check[x*3]=x;
		if(ar[x*2]>ar[x]+1)ar[x*2]=ar[x]+1,check[x*2]=x;
		if(ar[x+1]>ar[x]+1)ar[x+1]=ar[x]+1,check[x+1]=x;
	}
	cout<<ar[N]<<endl;
	array=N;
	while(array!=0)
	{
		cout<<array<<" ";
		array=check[array];
	}
}