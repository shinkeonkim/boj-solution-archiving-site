#include <iostream>
using namespace std;
int ar[5],Min=987654321;
int f(int a,int b)
{
	return b>0?f(b,a%b):a;
}
int main()
{
	for(int x=0; x<5; x++) cin>>ar[x];
	for(int x=0; x<5; x++)
	{
		for(int y=x+1; y<5; y++)
		{
			for(int z=y+1; z<5; z++)
			{
				int K=(ar[x]/f(ar[x],ar[y])*ar[y]);
				K=K*ar[z]/f(K,ar[z]);
				if(K<Min) Min=K;
			}
		}
	}	
	cout<<Min;
}