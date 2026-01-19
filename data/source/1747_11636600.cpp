#include <iostream>
#include <queue>
#include <deque>
#define M 1200000
using namespace std;
int N;
bool ar[11000000];
queue <int> que;
deque <int> Q;
bool f(int X)
{
	int x=X;
	while(!Q.empty()) Q.pop_back();
	while(x>0)
	{
		Q.push_back(x%10);
		x/=10;
	}
	while(!Q.empty())
	{
		if(Q.size()==1) return true;
		else 
		{
			if(Q.front()!=Q.back()) return false;
			else 
			{
				Q.pop_back();
				Q.pop_front();
			}
		}
	}
	return true;
}
int main()
{
	cin>>N;
	for(int x=1; x<=M; x++) ar[x]=true;
	ar[1]=false;
	for(int x=2; x<=M; x++)
	{
		if(ar[x])
		{	
			que.push(x);
			for(int y=x+x; y<=M; y+=x) ar[y]=false;
		}
	}
	while(!que.empty())
	{
		int A=que.front();
		que.pop();
		if(A>=N && f(A))
		{
			cout<<A;
			return 0;
		}
	}
	
}