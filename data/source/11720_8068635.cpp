#include <cstdio>
#include <iostream>
using namespace std;
int N,a,Sum;
int main()
{
	cin>>N;
	for(int x=0; x<N; x++)
	{
		scanf("%1d",&a);
		Sum+=a;
	}
	cout<<Sum;
}