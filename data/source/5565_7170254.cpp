#include <iostream>
using namespace std;
int Sum,A;
int main()
{
	cin>>Sum;
	for(int x=0; x<9; x++)
	{
		cin>>A;
		Sum-=A;
	}
	cout<<Sum;
} 