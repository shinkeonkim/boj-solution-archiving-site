#include <iostream>
using namespace std;
int N,a[1100],b[1100];
int main()
{
	cin>>N;
	for(int x=0; x<N; x++)
	{
		cin>>a[x];
		cin>>b[x];
	}
	for(int x=0; x<N; x++)
	{
		cout<<"Case #"<<x+1<<": "<<a[x]+b[x]<<endl;
	}
}