#include <iostream>
using namespace std;
int f(int x)
{
	int Sum=0;
	while(x>0)
	{
		Sum+=x%10;
		x/=10;
	}
	return Sum;
}
int main()
{
	int n,ans=0;
	cin>>n;
	for(int x=n; x>0; x--)
	{
		if(x+f(x)==n) ans=x;
	}
	if(ans>0) cout<<ans;
	else cout<<"0";
}