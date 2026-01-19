#include <iostream>
#include <string>
using namespace std;
string a[55];
int N,K;
int main()
{
	cin>>N;
	for(int x=0; x<N; x++) cin>>a[x];
	
	for(int x=0; x<a[0].length(); x++)
	{
		K=0;
		for(int y=1; y<N; y++)
		{
			if(a[0][x]!=a[y][x]) K=1;
		}
		if(K==0) cout<<a[0][x];
		else cout<<"?";
	}
}