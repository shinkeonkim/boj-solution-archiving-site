#include <iostream>
using namespace std;
int N;
int main()
{
	cin>>N;
	for(int x=N; x>=1; x--)
	{
		for(int y=1; y<=N-x; y++) cout<<" ";
		for(int y=1; y<=2*x-1; y++)cout<<"*";
		cout<<endl;
	}
	for(int x=2; x<=N; x++)
	{
		for(int y=1; y<=N-x; y++) cout<<" ";
		for(int y=1; y<=2*x-1; y++)cout<<"*";
		cout<<endl;
	}
}