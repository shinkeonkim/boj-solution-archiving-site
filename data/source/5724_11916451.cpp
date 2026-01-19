#include <iostream>
using namespace std;
long long N;
int main()
{
	while(1)
	{
		cin>>N;
		if(N==0) return false;
		cout<<N*(N+1)*(2*N+1)/6<<endl;	
	}
} 