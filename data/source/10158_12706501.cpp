#include <iostream>
using namespace std;
long long W,H,P,Q,T;
int main()
{
	cin>>W>>H>>P>>Q>>T;
	P=P+T;
	Q=Q+T;
	
	long long A=P/W;
	if(P%W>0) A++;
	
	if(A%2==0)
	{
		if(P%W==0) cout<<"0 ";
		else cout<<W-P%W<<" ";	
	}	
	else 
	{
		if(P%W==0) cout<<W<<" ";
		else cout<<P%W<<" ";
	}
	
	long long B=Q/H;
	if(Q%H>0) B++;
	
	if(B%2==0)
	{
		if(Q%H==0) cout<<"0 ";
		else cout<<H-Q%H;
	}
	else
	{
		if(Q%H==0) cout<<W<<" ";
		else cout<<Q%H;
	}
	
} 
