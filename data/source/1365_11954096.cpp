#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int N,ar[110000],S;
vector <int> V;
int main()
{
	cin>>N;
	for(int x=0; x<N; x++) cin>>ar[x];
	V.push_back(-1); // -INF 삽입 
	for(int x=0; x<N; x++)
	{
		if(V.back() < ar[x])
		{
			V.push_back(ar[x]);
			S++;
		}
		else
		{
			auto it = lower_bound(V.begin(),V.end(),ar[x]);
			*it = ar[x];
		}
	}
	cout<<N-S;
}