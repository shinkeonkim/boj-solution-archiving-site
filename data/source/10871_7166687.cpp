#include <iostream>
using namespace std;
int N,K,ar[11000];
int main()
{
	cin>>N>>K;
	for(int x=0; x<N; x++)cin>>ar[x];
	for(int x=0; x<N; x++)
	{
		if(ar[x]<K)cout<<ar[x]<<" ";
	}
}