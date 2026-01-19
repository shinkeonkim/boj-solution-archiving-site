#include <iostream>
#include <string>
using namespace std;
string a[220000];
int N;
int main()
{
	cin>>N;
	for(int x=0; x<N; x++)cin>>a[x];
	for(int x=0; x<N; x++)
	{
		cout<<"String #"<<x+1<<endl;
		for(int y=0; y<a[x].length(); y++)
		{
			if(a[x][y]=='Z') cout<<'A';
			else cout<<(char)(a[x][y]+1);
		}
		cout<<endl<<endl;
	}
}