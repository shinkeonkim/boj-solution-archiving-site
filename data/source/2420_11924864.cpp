#include <iostream>
using namespace std;
long long A,B;
int main()
{
	cin>>A>>B;
	if(A-B>0) cout<<A-B;
	else cout<<B-A;
}