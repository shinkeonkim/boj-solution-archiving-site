#include <iostream>
using namespace std;
long long int R,C,N,A,B;
int main()
{
	cin>>R>>C>>N;
	A=R/N;
	B=C/N;
	if(R%N>0) A++;
	if(C%N>0) B++;
	cout<<A*B;
}