#include <iostream>
using namespace std;
int N;
int main()
{
	cin>>N;
	if(N==1)
	{
		cout<<"*";
		return 0;
	}
	for(int x=1; x<=N; x++)
	{
		for(int y=1; y<=N; y+=2)
		{
			if(y!=1)cout<<" ";
			cout<<"*";
		}
		cout<<endl;
		for(int z=2; z<=N; z+=2)
		{
			cout<<" *";
		}
		cout<<endl;
	}
}