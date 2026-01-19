#include <iostream>
#include <algorithm>
using namespace std;

struct st{
	int A,B;
};

int N,Cnt;
st ar[110];

bool compare(st a, st b)
{
	if(a.A>b.A) return true;
	else if(a.A==b.A)
	{
		if(a.B<b.B) return true;
	}
	return false;
}

int main()
{
	cin>>N;
	for(int x=0; x<N; x++) cin>>ar[x].A>>ar[x].B;
	sort(ar,ar+N, compare);
	for(int x=5; x<N; x++)
	{
		if(ar[4].A==ar[x].A) Cnt++;
	}
	cout<<Cnt;
}