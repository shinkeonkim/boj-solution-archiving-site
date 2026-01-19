#include <iostream>
using namespace std;
int N;
int main()
{
	cin>>N;
	for(int x=1; x<=110; x++)
	{
		if(x*(x+1)==N-1)
		{
			cout<<x;
			return 0;
		}
	}
}