#include <iostream>
using namespace std;
int A,B;
int main()
{
	while(1)
	{
		cin>>A>>B;
		if(A==0&&B==0) return 0;
		else
		{
			if(A>B) cout<<"Yes\n";
			else cout<<"No\n";
		}
	}
}