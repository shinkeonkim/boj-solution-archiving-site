#include <iostream>
#include <queue>
#include <stack>
using namespace std;
int N,Cnt;
int ar[10]; 
int main()
{
	cin>>N;
	for(int x=0; x<5; x++)
	{
		cin>>ar[x];
		if(ar[x]==N) Cnt++;
	}
	cout<<Cnt;
}