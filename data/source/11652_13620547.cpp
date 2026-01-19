#include <iostream>
#include <algorithm>
using namespace std;
long long N,ar[1100000],Cnt,K,Max,Max_num;
int main()
{
	cin>>N;
	for(int x=0; x<N; x++)cin>>ar[x];
	sort(ar,ar+N);
	Cnt=1;
	K=ar[0];
	Max=1;
	Max_num=ar[0];
	for(int x=1; x<N; x++)
	{
		if(ar[x]==K)
		{
			Cnt++;
            if(Cnt>Max)
			{
				Max_num=K;
				Max=Cnt;
			}
		}
		else if(ar[x]!=K)
		{
			K=ar[x];
			Cnt=1;
		}
	}
    if(Cnt>Max)
	{
		Max_num=K;
	}
	cout<<Max_num;
}