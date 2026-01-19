#include <iostream>
#include <queue>
using namespace std;
struct st1
{
	int X,Y,Z,N;	
};
int M,N,H,ar[120][120][120],Max;//M가로 N세로 ar 가로 세로 높이 
queue <st1> qu;
int main()
{
	scanf("%d %d %d",&M,&N,&H);
	for(int z=0; z<H; z++)
	{
		for(int y=0; y<N; y++)
		{
			for(int x=0; x<M; x++)
			{
				scanf("%d",&ar[x][y][z]);
				if(ar[x][y][z]==0)ar[x][y][z]=2;
				else if(ar[x][y][z]==1)
				{
					st1 A;
					A.X=x; A.Y=y; A.Z=z; A.N=0;
					qu.push(A);
				}
			}	
		}	
	}
	
	while(!qu.empty())
	{
		st1 B;
		B=qu.front();
		if(B.X+1<M&&ar[B.X+1][B.Y][B.Z]==2)
		{
			st1 C;
			C.X=B.X+1; C.Y=B.Y; C.Z=B.Z; C.N=B.N+1;
			if(C.N>Max)Max=C.N;
			ar[C.X][C.Y][C.Z]=1;
			//printf("%d %d %d\n",C.X,C.Y,C.Z);
			qu.push(C);
		}
		if(B.X-1>-1&&ar[B.X-1][B.Y][B.Z]==2)
		{
			st1 C;
			C.X=B.X-1; C.Y=B.Y; C.Z=B.Z; C.N=B.N+1;
			if(C.N>Max)Max=C.N;
			ar[C.X][C.Y][C.Z]=1;
			//printf("%d %d %d\n",C.X,C.Y,C.Z);
			qu.push(C);
		}
		if(B.Y+1<N&&ar[B.X][B.Y+1][B.Z]==2)
		{
			st1 C;
			C.X=B.X; C.Y=B.Y+1; C.Z=B.Z; C.N=B.N+1;
			if(C.N>Max)Max=C.N;
			ar[C.X][C.Y][C.Z]=1;
			//printf("%d %d %d\n",C.X,C.Y,C.Z);
			qu.push(C);
		}
		if(B.Y-1>-1&&ar[B.X][B.Y-1][B.Z]==2)
		{
			st1 C;
			C.X=B.X; C.Y=B.Y-1; C.Z=B.Z; C.N=B.N+1;
			if(C.N>Max)Max=C.N;
			ar[C.X][C.Y][C.Z]=1;
			//printf("%d %d %d\n",C.X,C.Y,C.Z);
			qu.push(C);
		}
		if(B.Z+1<H&&ar[B.X][B.Y][B.Z+1]==2)
		{
			st1 C;
			C.X=B.X; C.Y=B.Y; C.Z=B.Z+1; C.N=B.N+1;
			if(C.N>Max)Max=C.N;
			ar[C.X][C.Y][C.Z]=1;
			//printf("%d %d %d\n",C.X,C.Y,C.Z);
			qu.push(C);
		}
		if(B.Z-1>-1&&ar[B.X][B.Y][B.Z-1]==2)
		{
			st1 C;
			C.X=B.X; C.Y=B.Y; C.Z=B.Z-1; C.N=B.N+1;
			if(C.N>Max)Max=C.N;
			ar[C.X][C.Y][C.Z]=1;
			//printf("%d %d %d\n",C.X,C.Y,C.Z);
			qu.push(C);
		}
		qu.pop();
	}
	
	int Cnt=0;
	for(int z=0; z<H; z++)
	{
		for(int y=0; y<N; y++)
		{
			for(int x=0; x<M; x++)
			{
				if(ar[x][y][z]==2) Cnt++;
			}	
		}	
	}
	if(Cnt>0)printf("-1");
	else printf("%d",Max);
} 