#include <iostream>
using namespace std;
int N,A[55],B[55];
int main()
{
	cin>>N;
	A[0]=1;
	B[0]=0;
	for(int x=1; x<=N; x++)
	{
		A[x]=B[x-1];
		B[x]=A[x-1]+B[x-1];
	}
	cout<<A[N]<<" "<<B[N];
}