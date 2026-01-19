#include <iostream>
using namespace std;
typedef long long ll;
ll ar[1100000];
ll f(ll x){
	if(ar[x]) return ar[x];
	else if(x==1) return ar[x]=0;
	else if(x==2) return ar[x]=1;
	else return ar[x]=((x-1)*(f(x-1)+f(x-2)))%1000000000;
}
int main()
{
	ll n;
	cin>>n;
	cout<<f(n);
}