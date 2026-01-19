#include <iostream>
using namespace std;
int N,K,C;
int main()
{
	cin>>N>>K;
	for(int x=1; x<=N; x++)
	{
		if(N%x==0) C++;
		if(C==K)
		{
			cout<<x;
			return 0;
		}
	}
	cout<<0;
}