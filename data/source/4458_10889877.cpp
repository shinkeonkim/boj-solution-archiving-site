#include <iostream>
#include <string>
using namespace std;
int N;
string ar[110000];
int main()
{
	cin>>N;;
	getline(cin,ar[0]);
	for(int x=0; x<N; x++)
	{
		getline(cin,ar[x]);	
	}
	for(int x=0; x<N; x++)
	{
		if(97<=ar[x][0]&&ar[x][0]<=122) ar[x][0]-=32;
	}
	for(int x=0; x<N; x++)
	{
		cout<<ar[x]<<endl;
	}
}