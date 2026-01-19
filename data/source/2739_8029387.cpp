#include <iostream>
using namespace std;
int N;
int main()
{
	cin>>N;
	for(int x=1; x<=9; x++)
	{
		cout<<N<<" * "<<x<<" = "<<N*x<<endl;
	}
}