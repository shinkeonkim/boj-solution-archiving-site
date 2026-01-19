#include <iostream>
using namespace std;
int N,K,S;
int ar[110];
int main()
{
	cin>>N>>K;
	for(int x=0 ;x<K; x++) cin>>ar[x];
	for(int x=0; x<K; x++)
	{
		S+=ar[x]/2;
		if(ar[x]%2!=0) S++;
	}
	if(S>=N)
	{
		cout<<"YES";
	}
	else cout<<"NO";
}