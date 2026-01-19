#include <iostream>
#include <algorithm>
using namespace std;
int N,ar[110000],Max;
bool compare(int a,int b)
{
	if(a>b) return true;
	return false;
}
int main()
{
	cin>>N;
	for(int x=0; x<N; x++) cin>>ar[x];
	sort(ar,ar+N,compare);
	for(int x=0; x<N; x++)
	{
		if(Max<(x+1)*ar[x])Max=(x+1)*ar[x];
	}
	cout<<Max;
}