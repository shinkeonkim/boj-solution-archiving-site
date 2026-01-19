#include <iostream>
using namespace std;
unsigned long long int N,ar[40];
int main()
{
	cin>>N;
	ar[0]=1;
	ar[2]=3;
	for(int x=4; x<=N; x+=2)
	{
		long long int Sum=ar[x-2]*3;
		for(int z=4; x-z>=0; z+=2)
		{
			Sum+=ar[x-z]*2;
		}
		ar[x]=Sum;
	}
	cout<<ar[N];
}