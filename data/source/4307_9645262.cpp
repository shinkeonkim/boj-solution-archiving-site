#include <iostream>
using namespace std;
int T,A,N,a,Max,Min;
int main()
{
	cin>>T;
	for(int x=0; x<T; x++)
	{
		Max=0,Min=0;
		cin>>A>>N;
		for(int y=0; y<N; y++)
		{
			cin>>a;
			Max=max(Max,max(a,A-a));
			Min=max(Min,min(a,A-a));
		}
		cout<<Min<<" "<<Max<<endl;
	}
}