#include <iostream>
using namespace std;
int ar[10];
long long n;
int main()
{
	cin>>n;
	while(n>0)
	{
		ar[n%10]++;
		n/=10;
	} 
	for(int x=9; x>-1; x--)
	{
		if(ar[x]>0)
		{
			for(int y=0; y<ar[x]; y++)
			{
				cout<<x;
			}
		}
	}
}