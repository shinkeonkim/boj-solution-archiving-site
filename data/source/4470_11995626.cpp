#include <iostream>
#include <string>
using namespace std;
int N;
string ar[110000];
int main()
{
	cin>>N;
	getline(cin,ar[0]);
	for(int x=0; x<N; x++) getline(cin,ar[x]);
	for(int x=0; x<N; x++) cout<<x+1<<". "<<ar[x]<<"\n";
}