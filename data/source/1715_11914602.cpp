#include <iostream>
#include <queue>
using namespace std;
priority_queue <int, vector<int>, greater<int> > Q;
int N,A,B,Z;
int main()
{
	cin>>N;
	for(int x=0; x<N; x++)
	{
		cin>>A;
		Q.push(A);
	}
	while(Q.size()>1)
	{
		A=Q.top();
		Q.pop();
		B=Q.top();
		Q.pop();
		Q.push(A+B);
		Z+=A+B;
	}
	cout<<Z;
}