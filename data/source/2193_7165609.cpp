#include <iostream>
using namespace std;
long long int ar[110],N;
int main()
{
	cin>>N;
	ar[1]=1;
	ar[2]=1; 
	for(int x=3; x<=N; x++) ar[x]=ar[x-1]+ar[x-2];
	cout<<ar[N];
} 