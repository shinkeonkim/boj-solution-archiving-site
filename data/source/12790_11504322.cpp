#include <iostream>
using namespace std;
int N,S,A;
int a[10];
int main()
{
	cin>>N;
	for(int i=0; i<N; i++)
	{
		S=0;
		for(int x=0; x<8; x++)
		{
			cin>>a[x];
		}
		A=a[0]+a[4];
		if(A<=1) A=1;
		S+=A;
		
		A=a[1]+a[5];
		if(A<=1) A=1;
		S+=5*A;
		
		A=a[2]+a[6];
		if(A<=0) A=0;
		S+=2*A;
		
		A=a[3]+a[7];
		S+=2*A;
		
		cout<<S<<endl;
	}
}