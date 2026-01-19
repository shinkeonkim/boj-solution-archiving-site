#include <iostream>
#include <string>
using namespace std;
int N,A;
string a;
int main()
{
	cin>>N;
	for(int x=0; x<N; x++)
	{
		cin>>A>>a;
		for(int x=0; x<a.length(); x++)
		{
			if(x+1==A);
			else cout<<a[x];
		}
		cout<<endl;
	}
}