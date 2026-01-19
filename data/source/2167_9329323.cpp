#include <iostream>
using namespace std;
struct st{
	int a,b,c,d;
};
int N,M,ar[330][330],DP[330][330],Q;
st q[11000];
int main()
{
	cin>>N>>M;
	for(int x=0; x<N; x++)
	{
		for(int y=0; y<M; y++) cin>>ar[x][y];
	}
	cin>>Q;
	for(int x=0; x<Q; x++)
	{
		cin>>q[x].a>>q[x].b>>q[x].c>>q[x].d;
		q[x].a--;
		q[x].b--;
		q[x].c--;
		q[x].d--;
	}
	
	for(int x=0; x<N; x++)
	{
		DP[x][0]=ar[x][0];
		for(int y=1; y<M; y++)
		{
			DP[x][y]=ar[x][y]+DP[x][y-1];
		}
	}
	
	for(int x=1; x<N; x++)
	{
		for(int y=0; y<M; y++)
		{
			DP[x][y]+=DP[x-1][y];
		}
	}
	
	/*for(int x=0; x<N; x++)
	{
		for(int y=0; y<M; y++)
		{
			cout<<DP[x][y]<<" ";
		}
		cout<<endl;
	}*/
	for(int x=0; x<Q; x++)
	{
		int Sum=0;
		Sum=DP[q[x].c][q[x].d];
		//cout<<"+ "<<DP[q[x].c][q[x].d];
		if(q[x].a>0)
		{
			Sum-=DP[q[x].a-1][q[x].d];
			//cout<<"- "<<DP[q[x].a-1][q[x].d];
		}
		if(q[x].b>0)
		{
			Sum-=DP[q[x].c][q[x].b-1];
			//cout<<"- "<<DP[q[x].c][q[x].b-1];
		}
		if(q[x].b>0&&q[x].a>0)
		{
			Sum+=DP[q[x].a-1][q[x].b-1];
			//cout<<"+ "<<DP[q[x].a-1][q[x].b-1];
		}
		cout<<Sum<<endl;
	}
}