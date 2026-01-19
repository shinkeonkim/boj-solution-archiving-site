#include <iostream>
#include <algorithm>
using namespace std;
int ar[9],S;
int main()
{
	for(int x=0; x<9; x++)
    {
        cin>>ar[x];
        S+=ar[x];
    }
	sort(ar,ar+9);
	for(int x=0; x<9; x++)
	{
		for(int y=x+1; y<9; y++)
		{
			if(S-ar[x]-ar[y]==100)
			{
				for(int z=0; z<9; z++)
				{
					if(z!=x&&z!=y) cout<<ar[z]<<"\n";
				}
                return 0;
			}
		}
	}
}