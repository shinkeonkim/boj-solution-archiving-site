#include <iostream>
#include <algorithm>
using namespace std;
long long int N,K,ar[330000],A[330000],S;
int main()
{
	cin>>N>>K;
	for(int x=0; x<N; x++) cin>>ar[x];
	for(int x=0; x<N-1; x++)
	{
		A[x]=ar[x+1]-ar[x];
	}
	sort(A,A+N-1);
	for(int x=0; x<N-K; x++) S+=A[x];
	cout<<S;
}