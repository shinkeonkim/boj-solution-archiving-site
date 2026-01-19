#include <iostream>
using namespace std;
int ar[11],S;
int main()
{
	for(int x=1; x<=9; x++) 
	{
		cin>>ar[x];
		S+=ar[x];
	}
	
	for(int x=1; x<=9; x++)
	{
		for(int y=x+1; y<=9; y++)
		{
			if(S-ar[x]-ar[y]==100)
			{
				for(int z=1; z<=9; z++)
				{
					if(z!=x&&z!=y) cout<<ar[z]<<endl;	
				}
				return 0;	
			}
		}
	}
}