#include <iostream>
#include <cstdio>
using namespace std;
int N,a,b;
int main()
{
	cin>>N;
	for(int x=0; x<N; x++)
	{
		cin>>a>>b;
		printf("You get %d piece(s) and your dad gets %d piece(s).\n",a/b,a%b);
	}
}