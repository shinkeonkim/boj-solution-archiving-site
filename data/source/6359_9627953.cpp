#include <iostream>
using namespace std;
int T,N,ar[110];
int main()
{
	cin>>T;
	for(int x=0; x<T; x++)
	{
		int Cnt=0;
		cin>>N;
		for(int x=1; x*x<=N; x++) Cnt++;
		cout<<Cnt<<endl;
	}
}