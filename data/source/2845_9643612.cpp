#include <iostream>
using namespace std;
int n,m,ar[10];
int main()
{
	cin>>n>>m;
	for(int x=0; x<5; x++)cin>>ar[x];
	for(int x=0; x<5; x++)cout<<ar[x]-n*m<<" ";
}