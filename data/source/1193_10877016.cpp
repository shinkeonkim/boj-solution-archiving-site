#include <iostream>
using namespace std;
int N,k,A,S,a,b;
int main()
{
	cin>>N;
	while(S<N)
	{
		k++;
		S+=k;
	}
	A=k+1;
	S-=k;
	//cout<<S<<" "<<A;
	if(k%2==0)
	{
		a=1,b=A-a;
		S++;
		while(S<N)
		{
			a++;
			b--;
			S++;
		}
	}
	else
	{
		a=A-1,b=1;
		S++;
		while(S<N)
		{
			a--;
			b++;
			S++;
		}
	}
	
	cout<<a<<"/"<<b;
	
}