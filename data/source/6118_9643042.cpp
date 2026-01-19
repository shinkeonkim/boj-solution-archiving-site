#include <iostream>
#include <queue>
#include <vector>
#define Mx 9999999
using namespace std;

struct st{
	int Node,Cost;
};

struct cmp{
	bool operator()(st A,st B)
	{
		return A.Cost>B.Cost;
	}
};

priority_queue <st, vector<st>, cmp> que;
vector < vector<st> > Edge(51000);
int N,M,a,b,check[55000],Min[55000],ans1,ans2,ans3;
st Z,Q;
int main()
{
	cin>>N>>M;
	for(int x=0; x<M; x++)
	{
		cin>>a>>b;
		Z.Cost=1;
		Z.Node=b;
		Edge[a].push_back(Z);
		Z.Node=a;
		Edge[b].push_back(Z);
	}	
	Q.Node=1;
	Q.Cost=0;
	que.push(Q);
	for(int x=2; x<=N; x++) Min[x]=Mx;
	for(int x=1; x<=N; x++)
	{
		Q=que.top();
		check[Q.Node]=1;
		for(int x=0; x<Edge[Q.Node].size(); x++)
		{
			if(check[Edge[Q.Node][x].Node]!=1&&Min[Edge[Q.Node][x].Node]>Min[Q.Node]+Edge[Q.Node][x].Cost)
			{
				Min[Edge[Q.Node][x].Node]=Min[Q.Node]+Edge[Q.Node][x].Cost;
				Z.Cost=Min[Q.Node]+Edge[Q.Node][x].Cost;
				Z.Node=Edge[Q.Node][x].Node;
				que.push(Z);
			}
		}
		que.pop();
	}
	
	for(int x=1; x<=N; x++)
	{
		if(ans2<Min[x])
		{
			ans2=Min[x];
			ans1=x;
		}
	}
	for(int x=1; x<=N; x++)
	{
		if(ans2==Min[x])ans3++;
	}
	cout<<ans1<<" "<<ans2<<" "<<ans3;
}