#include <iostream>
using namespace std;
int A[1100],B[1100],C[1100],N,K,Cnt=1;
int a,b,c,d;
int main()
{
	cin>>N>>K;
	for(int x=0; x<N; x++)
	{
		cin>>a>>b>>c>>d;
		A[a]=b;
		B[a]=c;
		C[a]=d;
	}
	
	for(int x=1; x<=N; x++)
	{
		if(x!=K)
		{
			if(A[x]>A[K]) Cnt++;
			else if(A[x]==A[K])
			{
				if(B[x]>B[K]) Cnt++;
				else if(B[x]==B[K])
				{
					if(C[x]>C[K]) Cnt++;
				}
			}
		}
	}
	cout<<Cnt;
}