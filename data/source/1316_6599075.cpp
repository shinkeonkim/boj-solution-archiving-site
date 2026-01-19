#include <iostream>
#include <string>
using namespace std;
string ar[110];
int check[500],Cnt,N;
int main()
{
	cin>>N;
	for(int x=0; x<N; x++) cin>>ar[x];
	
	for(int x=0; x<N; x++)
	{
		for(int z=0; z<500; z++) check[z]=0;
		
		check[ar[x][0]]=1;
		int aCnt=0;
		for(int y=1; y<ar[x].length(); y++)
		{
			if(ar[x][y]!=ar[x][y-1])
			{
				if(check[ar[x][y]]==1) aCnt=1;
				else check[ar[x][y]]=1;
			}
			else check[ar[x][y]]=1;
		}
		Cnt+=aCnt;
	}
	cout<<N-Cnt;
}