#include <iostream>
using namespace std;
int check[1100000];
int A,K,P,Cnt=1;
int main()
{
	cin>>A>>K;
	while(check[A]==0)
	{
		check[A]=Cnt;
		int X=A;
		A=0;
		while(X>0)
		{
			int z=1;
			for(int k=0; k<K; k++) z*=X%10;
			A+=z;
			X/=10;
		}
		Cnt++;
	}
	cout<<check[A]-1;
}