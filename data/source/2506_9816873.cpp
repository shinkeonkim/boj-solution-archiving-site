#include <iostream>
using namespace std;
int N,ar[110],Sum,Cnt;
int main()
{
	cin>>N;
	for(int x=0; x<N; x++)cin>>ar[x];
	for(int x=0; x<N; x++)
	{
		if(ar[x]==1)
		{
			Cnt++;
		}
		else if(ar[x]==0) Cnt=0;
		Sum+=Cnt;
	}
	cout<<Sum;
}