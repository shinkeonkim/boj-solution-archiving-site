#include <iostream>
using namespace std;
unsigned long long int T,N,ar[110]={0,1,1,1,2,2,3,4,5};
int main()
{
	for(int x=8; x<=100; x++)
	{
		ar[x]=ar[x-5]+ar[x-1];
	}
	cin>>T;
	for(int x=0; x<T; x++)
	{
		cin>>N;
		cout<<ar[N]<<endl;
	}
}