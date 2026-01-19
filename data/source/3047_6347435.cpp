#include <iostream>
#include <algorithm>
using namespace std;
int ar[3],x;
char arr[3];
int main()
{
	for(x=0; x<3; x++)cin>>ar[x];
	cin>>arr;
	sort(ar,ar+3);
	for(x=0; x<3; x++)
	{
		switch(arr[x])
		{
			case 'A':cout<<ar[0];
				break;
			case 'B':cout<<ar[1];
				break;
			case 'C':cout<<ar[2];
				break;
		}
		cout<<" ";
	}
}