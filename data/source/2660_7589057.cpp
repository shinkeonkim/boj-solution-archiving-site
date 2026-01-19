#include <iostream>
#define Mx 99999999
using namespace std;
int N,ar[60][60],a,b,arr[60],TotalMin=Mx,TotalCnt;
int main()
{
	
	cin>>N;
	cin>>a>>b;
	for(int x=0; x<=N; x++)
		for(int y=0; y<=N; y++) ar[x][y]=Mx;
	while(a!=-1&&b!=-1)
	{
		ar[a][b]=1;
		ar[b][a]=1;
		cin>>a>>b;
	}
	
	for(int x=1; x<=N; x++)
		for(int y=1; y<=N; y++)
			for(int z=1; z<=N; z++)
			{
				if(ar[y][x]+ar[x][z]<ar[y][z])
				{
					ar[y][z]=ar[y][x]+ar[x][z];
				}
			}
	
	for(int x=1; x<=N; x++)
	{
		int Max=0;
		for(int y=1; y<=N; y++)
		{
			if(x!=y && ar[x][y]!=Mx)
			{
				if(Max<ar[x][y])
					Max=ar[x][y];
			}
		}
		arr[x]=Max;
		if(Max<TotalMin) TotalMin=Max;
	}
	for(int x=1; x<=N; x++) if(arr[x]==TotalMin)TotalCnt++;
	cout<<TotalMin<<" "<<TotalCnt<<endl;
	for(int x=1; x<=N; x++)
	{
		if(arr[x]==TotalMin) cout<<x<<" ";
	}
}