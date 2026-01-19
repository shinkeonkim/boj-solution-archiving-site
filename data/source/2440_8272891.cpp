#include <iostream>
using namespace std;
int N;
int main()
{
	cin>>N;
	for(int x=N; x>-1; x--)
	{
		for(int y=0; y<x; y++) cout<<"*";
		cout<<endl;
	}
}