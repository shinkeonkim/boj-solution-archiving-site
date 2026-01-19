#include <iostream>
using namespace std;
int n,ar[100000],Memo[100000],Max=-99999999;
int bs(int x,int y)
{
	return x>y?x:y;
}
int f(int x)
{
	if(x==0) return ar[x];
	else if(Memo[x]) return Memo[x];
	else return Memo[x]=bs(f(x-1)+ar[x],ar[x]);
}
int main()
{
	cin>>n;
	for(int x=0; x<n; x++) cin>>ar[x];
	for(int x=0; x<n; x++)
	{
		if(Max<f(x)) Max=f(x);
	}
	cout<<Max;
}