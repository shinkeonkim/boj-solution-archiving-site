#include <iostream>
using namespace std;
int N;
int ar[110];
int main()
{
	cin>>N;
	for(int x=1; x<=N; x++) cin>>ar[x];
	for(int x=1; x<=N; x++)
	{
		ar[x]*=x;
	}
	for(int x=N; x>1; x--)
	{
		ar[x]-=ar[x-1];
	}
	for(int x=1; x<=N; x++) cout<<ar[x]<<" ";
}