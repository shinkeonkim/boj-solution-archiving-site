#include <iostream>
using namespace std;
long long A,B,C;
int main()
{
	cin>>A>>B>>C;
	if(B>=C)
	{
		printf("-1");
		return 0;
	}
	else
	{
		cout<<A/(C-B)+1;
	}
}