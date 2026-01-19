#include <iostream>
using namespace std;
int N,a,b,c;
int main()
{
	cin>>N;
	for(int x=0; x<N; x++)
	{
		cin>>a>>b>>c;
		if(a==b-c) cout<<"does not matter";
		else if(a>b-c) cout<<"do not advertise";
		else cout<<"advertise";
		cout<<endl;
	}
}