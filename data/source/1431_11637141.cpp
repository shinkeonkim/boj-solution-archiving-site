#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
struct st{
	string a;
	int K;
};
int N;
st ar[1100];
bool compare(st X, st Y)
{
	if(X.a.length()<Y.a.length()) return true;
	else if(X.a.length()==Y.a.length())
	{
		if(X.K<Y.K) return true;
		else if(X.K==Y.K)
		{
			if(X.a.compare(Y.a)<0) return true;
		}
	}
	return false;
}

int main()
{
	cin>>N;
	for(int x=0; x<N; x++) cin>>ar[x].a;
	for(int x=0; x<N; x++)
	{
		ar[x].K=0;
		for(int y=0; y<ar[x].a.length(); y++)
		{
			if('0'<=ar[x].a[y] && ar[x].a[y] <= '9')
			{
				ar[x].K+=ar[x].a[y]-'0';
			}
		}
	}
	sort(ar,ar+N,compare);
	for(int x=0; x<N; x++) cout<<ar[x].a<<endl;
}