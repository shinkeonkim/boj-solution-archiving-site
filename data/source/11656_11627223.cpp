#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;
vector <string> V;
string a,b;
int main()
{
	cin>>a;
	for(int x=0; x<a.length(); x++)
	{
		b=a[x];
		for(int y=x; y<a.length(); y++)
		{
			if(y!=x) b.push_back(a[y]);	
		}
		V.push_back(b);
	}
	sort(V.begin(),V.end());
	for(int x=0; x<V.size(); x++) cout<<V[x]<<endl;
}