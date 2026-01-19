#include <iostream>
#include <algorithm>
using namespace std;
int N,M;
int A[110000],B[110000];
int main()
{
	cin>>N;
	for(int x=0; x<N; x++)cin>>A[x];
	cin>>M;
	for(int x=0; x<M; x++)cin>>B[x];
	sort(A,A+N);
	for(int x=0; x<M; x++)
	{
		if(binary_search(A,A+N,B[x])) cout<<"1\n";
		else cout<<"0\n";
	}
}