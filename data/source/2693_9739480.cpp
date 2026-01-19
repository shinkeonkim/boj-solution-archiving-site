#include <iostream>
#include <algorithm>
using namespace std;
int T,ar[11],answer[1100];
int main()
{
	cin>>T;
	for(int w=0; w<T; w++)
	{
		for(int x=0; x<10; x++)cin>>ar[x];
		sort(ar,ar+10);
		answer[w]=ar[7];
	}
	for(int w=0; w<T; w++)cout<<answer[w]<<endl;
	
}