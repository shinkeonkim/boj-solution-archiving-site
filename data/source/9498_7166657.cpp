#include <iostream>
using namespace std;
int N;
int main()
{
	cin>>N;
	if(N>89)cout<<"A";
	else if(N>79)cout<<"B";
	else if(N>69)cout<<"C";
	else if(N>59)cout<<"D";
	else cout<<"F";
}