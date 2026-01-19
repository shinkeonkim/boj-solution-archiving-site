#include <iostream>
#include <queue>
using namespace std;
queue <int> q;
int A,B;
int main()
{
	cin>>A>>B;
	for(int x=1; x<=A; x++) q.push(x);
	cout<<"<";
	while(!q.empty())
	{
		for(int x=1; x<B; x++)
		{
			q.push(q.front());
			q.pop();
		}
		cout<<q.front();
		q.pop();
		if(q.size()>0)cout<<", ";
		else cout<<">";
	}
}