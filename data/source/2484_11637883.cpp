#include <iostream>
#include <algorithm>
using namespace std;
int N,ar[10],Max,K;
int main()
{
	cin>>N;
	for(int x=0; x<N; x++)
	{
		for(int y=0; y<4; y++) cin>>ar[y];
		sort(ar,ar+4);
		if(ar[0]==ar[1]&&ar[1]==ar[2]&&ar[2]==ar[3]) K=50000+ar[0]*5000;
		else if((ar[0]==ar[1]&&ar[1]==ar[2])||(ar[1]==ar[2]&&ar[2]==ar[3])) K=10000+ar[2]*1000;
		else if(ar[0]==ar[1]&&ar[2]==ar[3]) K=2000+ar[0]*500+ar[2]*500;
		else if(ar[0]==ar[1]) K=1000+ar[0]*100;
		else if(ar[1]==ar[2]) K=1000+ar[1]*100;
		else if(ar[2]==ar[3]) K=1000+ar[2]*100;
		else K=ar[3]*100;
		if(K>Max)Max=K;
	}
	cout<<Max;
}