#include <iostream>
#include <algorithm>
using namespace std;
unsigned long long int N,ar[55];
int main()
{
	cin>>N;
	for(int x=0; x<N; x++)cin>>ar[x];
	sort(ar,ar+N);
	if(N%2==1)
	{
		cout<<ar[N/2]*ar[N/2];
	}
	else
	{
		cout<<ar[0]*ar[N-1];
	}
}