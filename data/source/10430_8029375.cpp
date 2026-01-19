#include <iostream>
using namespace std;
int a,b,c;
int main()
{
	cin>>a>>b>>c;
	cout<<(a+b)%c<<endl<<(a%c+b%c)%c<<endl<<(a*b)%c<<endl<<(a%c*b%c)%c;
}