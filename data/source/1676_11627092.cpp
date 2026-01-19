#include <iostream>
using namespace std;
int N,A,B;
int main()
{
	cin>>N;
	for(int x=1; x<=N; x++)
	{
		int K=x;
		while(1)
		{
			if(K==0) break;
			if(K%2==0||K%5==0)
			{
				if(K%2==0) 
				{
					K/=2;
					A++;
				}
				else if(K%5==0)
				{
					K/=5;
					B++;
				}
			}
			else break;
		}
	}
	if(A>B) cout<<B;
	else cout<<A;
	
} 