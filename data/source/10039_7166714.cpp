#include <iostream>
using namespace std;
int Sum;
int main()
{
	for(int x=0; x<5; x++)
	{
		int a;
		cin>>a;
		if(a<40)Sum+=40;
		else Sum+=a;
	}
	cout<<Sum/5;
}