#include <iostream>
#include <string>
using namespace std;
int N;
string ar[110];
int main()
{
	cin>>N;
	for(int x=0; x<N; x++) cin>>ar[x];
	
	for(int x=0; x<N; x++)
	{
		for(int y=0; y<N; y++)
		{
			if(ar[x].length()==ar[y].length())
			{
				int C=1;
				for(int k=0; k<ar[x].length(); k++)
				{
					if(ar[x][k]!=ar[y][ar[y].length()-k-1])
					{
						
						C=0;
					}
				}
				
				if(C==1)
				{
					cout<<ar[x].length()<<" "<<ar[x][ar[x].length()/2];
					return 0;	
				}
			}
		}
	}
}