#include <iostream>
using namespace std;
int N,S;
int main()
{
	cin>>N;
	S=N/5;
	if(N%5!=0) S++;
	cout<<S;
}