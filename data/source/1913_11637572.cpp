#include <iostream>
using namespace std;
int dx[]={0,1,0,-1};
int dy[]={1,0,-1,0};
int D;
int ar[1100][1100];
int X=1,Y=1,N,K,A,B,k;
int main()
{
	cin>>N>>k;
	for(int K=N*N; K>=1; K--)
	{
		ar[Y][X]=K;
		D=D%4;
		if(Y+dy[D]<1||Y+dy[D]>N||X+dx[D]<1||X+dx[D]>N||ar[Y+dy[D]][X+dx[D]]!=0) D++;
		Y=Y+dy[D%4];
		X=X+dx[D%4];
	}
	for(int y=1; y<=N; y++)
	{
		for(int x=1; x<=N; x++)
		{
			cout<<ar[y][x]<<" ";
			if(ar[y][x]==k)
			{
				A=y;
				B=x;
			}
		}
		cout<<endl;
	}
	cout<<A<<" "<<B;
}