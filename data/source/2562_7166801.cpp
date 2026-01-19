#include <iostream>
using namespace std;
int PL,Max=0;
int main()
{
	for(int x=0; x<9; x++)
	{
		int a;cin>>a;
		if(a>Max)
		{
			Max=a;
			PL=x+1;
		}
	}
	cout<<Max<<endl<<PL;
}