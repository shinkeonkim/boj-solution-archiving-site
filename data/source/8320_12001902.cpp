#include <iostream>
using namespace std;
int N,S;
int main()
{
	cin>>N;
	for(int x=1; x*x<=N; x++)
	{
		for(int y=x; y<=N; y++)
		{
			if(x*y<=N) 
			{
				S++;
				//cout<<x<<" "<<y<<endl;
			}
		}
	}
	cout<<S;
} 