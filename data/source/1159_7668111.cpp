#include <iostream>
#include <string>
using namespace std;
int N,c=1,C[500];
string a[200];
int main()
{
	cin>>N;
	for(int x=0; x<N; x++) cin>>a[x];
	for(int x=0; x<N; x++)
	{
		C[a[x][0]]++;
	}
	for(int x='a'; x<'z'+1; x++)
	{
		if(C[x]>4)
		{
			cout<<(char)x;
			c=0;
		}
	}
	if(c==1) cout<<"PREDAJA";
}