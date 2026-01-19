#include <iostream>
#include <map>
#include <string>
#include <algorithm>

using namespace std;

map<string, int> Mp;

int N,M,Cnt;
string a;
string ar[550000];
int main()
{
	cin>>N>>M;
	for(int x=0; x<N+M; x++)
	{
		cin>>a;
		Mp[a]++;
	}
	map <string, int> ::iterator iter;
	for(iter = Mp.begin(); iter !=Mp.end(); iter++)
	{
		if(iter->second == 2)
		{
			ar[Cnt++]=iter -> first;
		}
	}
	cout<<Cnt<<endl;
	sort(ar,ar+Cnt);
	for(int x=0; x<Cnt; x++) cout<<ar[x]<<endl;
}