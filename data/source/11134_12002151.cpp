#include <iostream>
using namespace std;
int T,N,C;
int main()
{
	cin>>T;
	for(int x=0; x<T; x++)
	{
		cin>>N>>C;
		int S=N/C;
		if(N%C!=0) S++;
		cout<<S<<endl;
	}
}