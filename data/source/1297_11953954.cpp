#include <iostream>
#include <cmath>
using namespace std;
double L,a,b,K,k;
int main()
{
	cin>>L>>a>>b;
	K=L*L/(a*a+b*b);
	k=sqrt(K);
	cout<<(int)(k*a)<<" "<<(int)(k*b);
}