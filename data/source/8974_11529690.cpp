#include <iostream>
using namespace std;
int A,B,S;
int ar[1100],K=1;
int main()
{
	cin>>A>>B;
	for(int x=1; x<=B; x++)
	{
		for(int y=0; y<K; y++)
		{
			ar[x]=K;
			x++;
		}
		K++;
		x--;
	}
	for(int x=A; x<=B; x++) S+=ar[x];
	cout<<S;
}