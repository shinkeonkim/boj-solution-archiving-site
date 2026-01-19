#include <iostream>
using namespace std;
long long N,ar[1100],K,Cnt;
int main()
{
	cin>>N;
	for(int x=0; x<N; x++) cin>>ar[x];
	cin>>K;
	
	for(int x=0; x<N; x++)
	{
		if(ar[x]!=0)
		{
			if(ar[x]%K==0) Cnt+=ar[x]/K;
			else Cnt+=ar[x]/K+1;
		}
	}
	
	cout<<Cnt*K; 
}