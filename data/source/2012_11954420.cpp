#include <iostream>
#include <algorithm>
using namespace std;
long long N,S;
long long ar[550000];
long long f(long long  x)
{
	return x>0?x:-x;
}
int main()
{
	cin>>N;
	for(int x=0; x<N; x++) cin>>ar[x];
	sort(ar,ar+N);
	for(int x=0; x<N; x++)
	{
		S+=f(ar[x]-(x+1));
	}
	cout<<S;
}