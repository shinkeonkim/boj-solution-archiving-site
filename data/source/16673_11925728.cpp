#include <iostream>
using namespace std;
long long C,K,P;
int main()
{
	cin>>C>>K>>P;
	cout<<(C*(C+1)/2)*K+(C*(C+1)*(2*C+1)/6)*P;
}