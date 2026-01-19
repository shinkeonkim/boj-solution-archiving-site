#include <iostream>
#define Mx 999999999
using namespace std;
int Min1=Mx,Min2=Mx,a;
int main()
{
	for(int x=0; x<3; x++)
	{
		cin>>a;
		if(a<Min1)Min1=a;
	}
	
	for(int x=0; x<2; x++)
	{
		cin>>a;
		if(a<Min2)Min2=a;
	}
	cout<<Min1+Min2-50;
}