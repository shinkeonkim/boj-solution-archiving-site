#include <iostream>
#include <queue>
#include <stack>
using namespace std;
int N,ar[110],Cnt;
int main()
{
	cin>>N;
	for(int x=0; x<N; x++)
	{
		cin>>ar[x];
	}
	for(int x=0; x<N; x++)
	{
		bool check=true;
		for(int y=2; y<ar[x]; y++)
		{
			if(ar[x]%y==0) check=false;
		}
		if(check&&ar[x]>1) Cnt++;
	}
	cout<<Cnt;
}