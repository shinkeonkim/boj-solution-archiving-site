#include <iostream>
using namespace std;
int A,B,ar[1100],Cnt=1,S;
int main()
{
	cin>>A>>B;
	for(int x=1; x<=B; x++)
	{
		for(int y=0; y<Cnt; y++)
		{
			ar[x]=Cnt;
			x++;
		}
		x--;
		Cnt++;
	}
	for(int x=A; x<=B; x++) S+=ar[x];
	cout<<S;
}