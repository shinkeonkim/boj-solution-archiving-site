#include <iostream>
using namespace std;
int A[10]={1,2,3,3,4,10},B[10]={1,2,2,2,3,5,10},T;
int a,b,S1,S2;
int main()
{
	cin>>T;
	for(int x=1; x<=T; x++)
	{
		S1=S2=0;
		for(int y=0; y<6; y++)
		{
			cin>>a;
			S1+=a*A[y];
		}
		for(int z=0; z<7; z++)
		{
			cin>>b;
			S2+=b*B[z];
		}
		cout<<"Battle "<<x<<": ";
		if(S1>S2)
		{
			cout<<"Good triumphs over Evil\n";
		}
		else if(S1<S2)
		{
			cout<<"Evil eradicates all trace of Good\n";
		}
		else
		{
			cout<<"No victor on this battle field\n";
		}
	}
}