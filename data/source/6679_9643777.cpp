#include <iostream>
using namespace std;
int A,B,C;
int f(int n,int k)
{
	int Sum=0;
	while(n>0)
	{
		Sum+=n%k;
		n/=k;
	}
	return Sum;
}
int main()
{
	for(int x=1000; x<=9999; x++)
	{
		A=f(x,10);
		B=f(x,12);
		C=f(x,16);
		
		if(A==B&&B==C)
		{
			cout<<x<<endl;	
		}
	}
}