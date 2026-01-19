#include<iostream>
#include <string>
#include <queue>
#include <vector>
#include <algorithm>
using namespace std;
string a,b;
queue <char> A;
queue <char> B;
vector <char> V;
int Cnt;
int main()
{
	cin>>a>>b;
	for(int x=0; x<a.length(); x++)
	{
		V.push_back(a[x]);
	}
	sort(V.begin(),V.end());
	for(int x=0; x<V.size(); x++) A.push(V[x]);
	for(int x=0; x<a.length(); x++) V.pop_back();
	
	for(int x=0; x<b.length(); x++)
	{
		V.push_back(b[x]);
	}
	sort(V.begin(),V.end());
	for(int x=0; x<V.size(); x++) B.push(V[x]);
	
	while(!A.empty()||!B.empty())
	{
		if(!A.empty()&&!B.empty())
		{
			if(A.front()==B.front())
			{
				A.pop();
				B.pop();	
			}	
			else if(A.front()>B.front())
			{
				B.pop();
				Cnt++;
			}
			else if(A.front()<B.front())
			{
				A.pop();
				Cnt++;
			}
		}
		else
		{
			if(!A.empty())
			{
				Cnt++;
				A.pop();
			}
			if(!B.empty())
			{
				Cnt++;
				B.pop();
			}
		}
	}
	cout<<Cnt;
 } 