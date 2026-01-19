#include <iostream>
#include <algorithm>
using namespace std;
int N,s,ar[1100],Max;
int main()
{
	cin>>N;
	s=0;
	for(int x=0; x<N; x++)cin>>ar[x];
	for(int x=1; x<N; x++)
	{
		if(ar[x-1]<ar[x])
		{
			Max=max(Max,ar[x]-ar[s]);
		}
		else 
		{
			s=x;
		}
	}
	cout<<Max;
}