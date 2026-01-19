#include <iostream>
using namespace std;
int A,Cnt,K;
int main()
{
	cin>>A;
	while(A>0)
	{
		K=1;
		while(K*2<=A) K*=2;
		Cnt++;
		A-=K;
	}
	cout<<Cnt;
}