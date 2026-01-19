#include <iostream>
using namespace std;
int ar[3300000],N;
int main()
{
	cin>>N;
	for(int x=2; x<=N; x++)ar[x]=99999999;
	for(int x=0; x<=N; x++)
	{
		if(ar[x+1]>ar[x]+1)ar[x+1]=ar[x]+1; 
		if(ar[x*2]>ar[x]+1)ar[x*2]=ar[x]+1;
		if(ar[x*3]>ar[x]+1)ar[x*3]=ar[x]+1;	
	}
	cout<<ar[N];
}