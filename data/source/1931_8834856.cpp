#include <iostream>
#include <algorithm>
using namespace std;

struct st{
	int a,b; 
};

int N,Cnt=1,End;

st ar[110000];

bool Compare(st A,st B)
{
	if(A.b<B.b) return true;
	else if(B.b == A.b && A.a<B.a) return true;
	return false;
}

int main()
{
	cin>>N;
	for(int x=0; x<N; x++)
	{
		cin>>ar[x].a>>ar[x].b;
	}
	
	sort(ar,ar+N,Compare);
	
	End=ar[0].b;
	for(int x=1; x<N; x++)
	{
		if(End<=ar[x].a)
		{
			Cnt++;
			End=ar[x].b;
			//cout<<ar[x].a<<" "<<ar[x].b<<endl;
		}
	}
	cout<<Cnt;
}