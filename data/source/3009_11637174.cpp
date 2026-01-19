#include <iostream>
#include <algorithm>
using namespace std;
int X[5],Y[5];
int main()
{
	for(int x=0; x<3; x++) cin>>X[x]>>Y[x];
	sort(X,X+3);
	sort(Y,Y+3);
	if(X[0]==X[1])
	{
		cout<<X[2]<<" ";
	}
	else cout<<X[0]<<" ";
	
	if(Y[0]==Y[1])
	{
		cout<<Y[2]<<" ";
	}
	else cout<<Y[0]<<" ";
}