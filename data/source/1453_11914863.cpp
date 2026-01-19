#include <iostream>
using namespace std;
int N,A,Cnt,ar[110];
int main()
{
	cin>>N;
	for(int x=0; x<N; x++)
	{
		cin>>A;
		if(ar[A]==1) Cnt++;
		else ar[A]=1;	
	}
	cout<<Cnt;
} 