#include <iostream>
#include <algorithm>
using namespace std;
int T;
int ar[11];
int main()
{
	cin>>T;
	for(int x=0; x<T; x++)
	{
		for(int y=0; y<5; y++) cin>>ar[y];
		sort(ar,ar+5);
		if(ar[3]-ar[1]>3) cout<<"KIN\n";
		else cout<<ar[1]+ar[2]+ar[3]<<endl;
	}
}