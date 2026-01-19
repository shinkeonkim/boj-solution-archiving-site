#include <iostream>
using namespace std;
int T;
int N,K,a,S;
int main()
{
	cin>>T;
	for(int w=0; w<T; w++)
	{
		S=0;
		cin>>N>>K;
		for(int x=0; x<N; x++)
		{
			cin>>a;
			S+=a/K;
		}
		cout<<S<<endl;
	}
}