#include <iostream>
using namespace std;
int M,K,A;
int main()
{
	for(int x=0; x<9; x++)
	{
		for(int y=0; y<9; y++)
		{
			cin>>A;
			if(A>M)
			{
				M=A;
				K=x*9+y;
			}
		}
	}
	cout<<M<<endl<<K/9+1<<" "<<K%9+1;
}