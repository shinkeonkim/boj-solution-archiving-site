#include <iostream>
using namespace std;
int A,K;
char B;
int main()
{
	cin>>A;
	while(1)
	{
		cin>>B;
		if(B=='=')
		{
			cout<<A;
			return 0;	
		}	
		else
		{
			cin>>K;
			if(B=='+')
			{
				A=A+K;
			}
			else if(B=='-')
			{
				A=A-K;
			}
			else if(B=='*')
			{
				A=A*K;
			}
			else if(B=='/')
			{
				A=A/K;
			}		
		}
	}	
}