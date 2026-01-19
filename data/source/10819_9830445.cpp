#include <iostream>
#include <algorithm>
using namespace std;
int N,Max;
int ar[10];
int abs(int a)
{
	return a>0?a:-a;
}
int main()
{
	cin>>N;
	for(int x=0; x<N; x++)cin>>ar[x];
	sort(ar,ar+N);
	while(next_permutation(ar,ar+N))
	{
		int Sum=0;
		for(int x=0; x<N-1; x++)
		{
			Sum+=abs(ar[x]-ar[x+1]);
		}
		if(Sum>Max)Max=Sum;
	}
	cout<<Max;
}