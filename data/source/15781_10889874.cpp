#include <iostream>
#include <algorithm>
using namespace std;
int N,M,A,B,a,b;
int main()
{
	cin>>N>>M;
	for(int x=0; x<N; x++)
	{
		cin>>a;
		A=max(A,a);
	}
	for(int x=0; x<M; x++)
	{
		cin>>b;
		B=max(B,b);
	}
	cout<<A+B;
}