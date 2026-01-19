#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
struct st{
	int A,B,C;
	string arr;
};

int N;
st ar[110000];

bool compare(st X,st Y)
{
	if(X.A>Y.A) return true;
	else if(X.A==Y.A)
	{
		if(X.B<Y.B) return true;
		else if(X.B==Y.B)
		{
			if(X.C>Y.C) return true;
			else if(X.C==Y.C)
			{
				if(X.arr.compare(Y.arr)<0) return true;
			}
		}
	}
	return false;
}
int main()
{
	cin>>N;
	for(int x=0; x<N; x++) cin>>ar[x].arr>>ar[x].A>>ar[x].B>>ar[x].C;
	sort(ar,ar+N,compare);
	for(int x=0; x<N; x++) cout<<ar[x].arr<<"\n";
}