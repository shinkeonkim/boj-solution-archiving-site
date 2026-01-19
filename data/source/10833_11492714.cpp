#include <iostream>
using namespace std;
int N,A,B,S;
int main()
{
	cin>>N;
	for(int x=0; x<N; x++)
	{
		cin>>A>>B;
		S+=B%A;
	}
	cout<<S;
}