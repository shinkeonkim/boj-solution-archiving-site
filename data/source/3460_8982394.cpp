#include<iostream>
using namespace std;
int T,ar[11],C;

int main()
{
	cin>>T;
	for(int x=0; x<T; x++) cin>>ar[x];
	for(int x=0; x<T; x++)
	{
		C=0;
		while(ar[x]>0)
		{
			if(ar[x]%2==1) cout<<C<<" ";
			C++;
			ar[x]/=2;
		}
		cout<<endl;
	}
}