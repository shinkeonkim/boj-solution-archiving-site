#include <iostream>
using namespace std;
long long int N,A,B,ar[1100000],Cnt;
int main()
{
	cin>>N;
	for(int x=0; x<N; x++) cin>>ar[x];
	cin>>A>>B;
	for(int x=0; x<N; x++)
	{
		Cnt++;
		ar[x]-=A;
		if(ar[x]>0)
		{
			if(ar[x]%B==0) Cnt+=(ar[x]/B);
			else Cnt+=(ar[x]/B)+1;	
		} 
	}
	cout<<Cnt;
}