#include <iostream>
using namespace std;
int N;
int main()
{
	cin>>N;
	for(int x=0; x<N; x++)
	{
		for(int y=0; y<x; y++) cout<<" ";
		for(int y=N-x; y>0; y--)
		{
			cout<<"*";
		}
		cout<<endl;
	}
}