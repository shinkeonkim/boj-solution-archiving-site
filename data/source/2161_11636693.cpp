#include <iostream>
#include <queue>
using namespace std;
int N;
queue <int> S;
int main()
{
	cin>>N;
	for(int x=1; x<=N; x++) S.push(x);
	
	while(!S.empty())
	{
		cout<<S.front()<<" ";
		S.pop();
		if(!S.empty()) 
		{
			S.push(S.front());
			S.pop();
		}
	}
}