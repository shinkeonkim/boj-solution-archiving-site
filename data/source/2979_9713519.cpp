#include <iostream>
using namespace std;
int Cost[4],Time[110],a,b,Sum;
int main()
{
	for(int x=1; x<4; x++) cin>>Cost[x];
	for(int x=0; x<3; x++)
	{
		cin>>a>>b;
		for(int x=a; x<b; x++)Time[x]++;
	}
	for(int x=1; x<=100; x++)
	{
		Sum+=Cost[Time[x]]*Time[x];
	}
	cout<<Sum;
}