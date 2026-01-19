#include <iostream>
#include <map>
#include <string>
#include <algorithm>
using namespace std;
map <string,string> M;
map <string,string>::iterator I;
int N,Cnt;
string a,b;
string ar[1100000];

bool compare(string a,string b)
{
	if(a.compare(b)>0) return true;
	return false;
}

int main()
{
	cin>>N;
	for(int x=0; x<N; x++)
	{
		cin>>a>>b;
		M[a]=b;
	}
	for (I=M.begin(); I!=M.end(); I++)
	{
		if((*I).second=="enter")
		{
			ar[Cnt++]=(*I).first;
		}
	}
	sort(ar,ar+Cnt,compare);
	for(int x=0; x<Cnt; x++) cout<<ar[x]<<"\n";
	
}