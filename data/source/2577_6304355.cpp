#include <iostream>
using namespace std;
int a,b,c,ar[10];
int main()
{
	cin>>a>>b>>c;
	a=a*b*c;
	while(a>0)
	{
		ar[a%10]++;
		a/=10;
	}
	for(int x=0; x<10; x++) cout<<ar[x]<<endl;
}