#include <iostream>
using namespace std;
long long int N,K,ar[110];
long long int f(long long int a,long long int b)
{
	return b>0?f(b,a%b):a;
}
int main()
{
	cin>>N;
	for(int t=0; t<N; t++)
	{
		long long int S=0;
		cin>>K;
		for(int x=0; x<K; x++) cin>>ar[x];
		for(int x=0; x<K; x++)
		{
			for(int y=x+1; y<K; y++)
			{
				S+=f(ar[x],ar[y]);
			}
		}
		cout<<S<<endl;
	}
}