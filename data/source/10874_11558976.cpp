#include <iostream>
using namespace std;
int N,a;
int main()
{
	cin>>N;
	for(int i=1; i<=N; i++)
	{
		bool F=true;
		for(int y=0; y<2; y++)
		{
			for(int x=1; x<=5; x++)
			{
				cin>>a;
				if(a!=x) F=false;
			}
		}
		if(F) cout<<i<<endl;
	}
 } 