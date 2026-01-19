#include <iostream>
using namespace std;
int N;
int main()
{
	cin>>N;
	for(int x=1; x<=N; x++)
	{
		for(int y=1; y<=N-x; y++)
		{
			cout<<" ";
		}
		for(int y=1; y<=x; y++)
		{
			cout<<"*";
		}
		cout<<endl;
	}
}