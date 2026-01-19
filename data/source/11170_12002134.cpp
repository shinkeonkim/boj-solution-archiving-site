#include <iostream>
using namespace std;
int T,N,M,S;
int f(int x)
{
	int Cnt=0;
	while(x>0)
	{
		if(x%10==0) Cnt++;
		x/=10;
	}
	return Cnt;
}
int main()
{
	cin>>T;
	for(int x=0; x<T; x++)
	{
		cin>>N>>M;
		S=0;	
		for(int x=N; x<=M; x++)
		{
			if(x!=0) S+=f(x);
			else S++;
		}
		cout<<S<<"\n";
	}
	
}