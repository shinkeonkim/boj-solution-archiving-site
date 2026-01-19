#include <iostream>
using namespace std;
int ar[11],S,M,K;
int main()
{
	for(int x=0; x<10; x++) cin>>ar[x];
	for(int x=0; x<10; x++) S+=ar[x];
	for(int x=0; x<10; x++)
	{
		int Cnt=0;
		for(int y=0; y<10; y++)
		{
			if(ar[x]==ar[y]) Cnt++;
		}
		if(Cnt>M)
		{
			K=ar[x];
			M=Cnt;
		}
	}
	cout<<S/10<<endl<<K;
}