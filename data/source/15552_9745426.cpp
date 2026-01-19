#include <iostream>
using namespace std;
int N,A,B;
int main()
{
	cin.tie(NULL);
	ios_base::sync_with_stdio(false);
	cin>>N;
	for(int x=0; x<N; x++)
	{
		cin>>A>>B;
		cout<<A+B<<"\n";
	}
}