#include <iostream>
using namespace std;
int N,Cnt,a;
int main()
{
	cin>>N;
	for(int x=0; x<N; x++)
	{
		cin>>a;
		if(a==1)Cnt++;
	}
	if(Cnt>N-Cnt) cout<<"Junhee is cute!";
	else cout<<"Junhee is not cute!";
}