#include <iostream>
using namespace std;
int N,Max;
int ar[20];
int main()
{
	cin>>N;
	if(N==0)
	{
		cout<<"1";
		return 0;
	}
	while(N>0)
	{
		if(N%10!=9)
		{
			ar[N%10]++;
		}
		else if(N%10==9) ar[6]++;
		N/=10;
	}
	for(int x=0; x<=9; x++)
	{
		if(x!=6)
		{
			 Max=Max<ar[x]?ar[x]:Max;
		}
		else if(x==6)
		{
			if(ar[x]%2==0) Max=Max<ar[x]/2?ar[x]/2:Max;
			else Max=Max<ar[x]/2+1?ar[x]/2+1:Max;
		}
	}
	cout<<Max;
}