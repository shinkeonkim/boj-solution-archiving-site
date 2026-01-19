#include <iostream>
using namespace std;
int M,S;
int ar[4][2];
int main()
{
	for(int x=0; x<4; x++)
	{
		for(int y=0; y<2; y++)
		{
			cin>>ar[x][y];
		}
	}
	
	for(int x=0; x<4; x++)
	{
		S+=-ar[x][0]+ar[x][1];	
		if(S>M) M=S;
	}
	cout<<M;
}