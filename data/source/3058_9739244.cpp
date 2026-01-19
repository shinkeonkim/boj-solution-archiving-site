#include <iostream>
using namespace std;
int T,ar[10],Sum,Min;
int main()
{
	cin>>T;
	for(int w=0; w<T; w++)
	{
		Sum=0,Min=100;
		for(int x=0; x<7; x++)cin>>ar[x];
		for(int x=0; x<7; x++)
		{
			if(ar[x]%2==0)
			{
				Sum+=ar[x];
				if(ar[x]<Min)Min=ar[x];
			}
		}
		cout<<Sum<<" "<<Min<<endl;
	}
}