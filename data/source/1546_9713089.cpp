#include <iostream>
#include <cstdio>
using namespace std;
int N;
double ar[1100];
double Max,Sum;
int main()
{
	cin>>N;
	for(int x=0; x<N; x++)cin>>ar[x];
	for(int x=0; x<N; x++)
	{
		if(Max<ar[x])Max=ar[x];
	}
	for(int x=0; x<N; x++)
	{
		Sum+=ar[x]/Max*100;
	}
	printf("%.2lf",(double)(Sum/N));
}