#include <iostream>
#include <algorithm>
using namespace std;
int N,ar[1100],Sum;
int main()
{
	cin>>N;
	for(int x=0; x<N; x++)cin>>ar[x];
	sort(ar,ar+N);
	Sum=ar[0];
	for(int x=1; x<N; x++)
	{
		ar[x]+=ar[x-1];
		Sum+=ar[x];
	}
	cout<<Sum;
}