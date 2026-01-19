#include <iostream>
#include <algorithm>
#include <functional>
using namespace std;
long long int N,ar[110000],S;
int main()
{
	cin>>N;
	for(int x=0; x<N; x++) cin>>ar[x];
	sort(ar,ar+N,greater<int>());	
	for(int x=0; x<N; x++)
	{
		if(ar[x]-x<0) ;
		else S+=ar[x]-x;
	}
	cout<<S;
}