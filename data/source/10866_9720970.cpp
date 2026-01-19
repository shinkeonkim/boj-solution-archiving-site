#include <iostream>
#include <deque>
#include <string>
using namespace std;
deque <int> dq;
int N,b;
string a;
int main()
{
	cin>>N;
	for(int x=0; x<N; x++)
	{
		cin>>a;
		if(a[0]=='p')
		{
			if(a[1]=='u')
			{
				if(a[5]=='b')
				{
					cin>>b;
					dq.push_back(b);
				}
				if(a[5]=='f')
				{
					cin>>b;
					dq.push_front(b);
				}
			}
			if(a[1]=='o')
			{
				if(a[4]=='f')
				{
					if(dq.empty()) cout<<"-1"<<endl;
					else 
					{	
						cout<<dq.front()<<endl;
						dq.pop_front();	
					}
				}
				if(a[4]=='b')
				{
					if(dq.empty()) cout<<"-1"<<endl;
					else
					{
						cout<<dq.back()<<endl;
						dq.pop_back();
					}
				}
			}
		}
		if(a[0]=='f')
		{
			if(dq.empty()) cout<<"-1"<<endl;
			else cout<<dq.front()<<endl;
		}
		
		if(a[0]=='b')
		{
			if(dq.empty()) cout<<"-1"<<endl;
			else cout<<dq.back()<<endl;
		}
		
		if(a[0]=='s')
		{
			cout<<dq.size()<<endl;
		}
		
		if(a[0]=='e')
		{
			if(dq.empty()) cout<<"1"<<endl;
			else cout<<"0"<<endl;
		}
	}
}