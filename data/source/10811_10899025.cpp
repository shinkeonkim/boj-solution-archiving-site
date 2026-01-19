#include <iostream>
#include <stack>
using namespace std;
int N,M,a,b,ar[110];
stack <int> st;
int main()
{
	cin>>N>>M;
	for(int x=1; x<=N; x++) ar[x]=x;
	for(int x=1; x<=M; x++)
	{
		cin>>a>>b;
		for(int x=a; x<=b; x++)
		{
			st.push(ar[x]);
		}
		for(int x=a; x<=b; x++)
		{
			ar[x]=st.top();
			st.pop();
		}
	}
	for(int x=1; x<=N; x++) cout<<ar[x]<<" ";
}