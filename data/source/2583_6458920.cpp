#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;
int M,N,K,ar[110][110],Cnt,check[100];
struct st{
	int xx,yy;
};
int main()
{
	scanf("%d %d %d",&M,&N,&K);
	for(int x=0; x<K; x++)
	{
		int a,b,c,d;
		scanf("%d %d %d %d",&a,&b,&c,&d);
		for(int X=a; X<c; X++)
		{
			for(int Y=b; Y<d; Y++)
			{
				ar[X][Y]=1;
			}
		}
	}
	/*for(int y=0; y<M; y++)
	{
		for(int x=0; x<N; x++)
		{
			printf("%d",ar[x][y]);
		}printf("\n");
	}*/
	for(int x=0; x<N; x++)
	{
		for(int y=0; y<M; y++)
		{
			if(ar[x][y]==0)
			{
				//printf("%d %d\n",x,y);
				st Z;
				Z.xx=x; Z.yy=y;
				queue <st> qu;
				qu.push(Z);
				int Cmt=0;
				while(!qu.empty())
				{
					st A;
					A=qu.front();
					if(A.yy+1<M&&ar[A.xx][A.yy+1]!=1)
					{
						st B;
						B.xx=A.xx; B.yy=A.yy+1;
						qu.push(B);
						ar[B.xx][B.yy]=1;
						Cmt++;
					}
					if(A.yy-1>-1&&ar[A.xx][A.yy-1]!=1)
					{
						st B;
						B.xx=A.xx; B.yy=A.yy-1;
						qu.push(B);
						ar[B.xx][B.yy]=1;
						Cmt++;
					}
					if(A.xx+1<N&&ar[A.xx+1][A.yy]!=1)
					{
						st B;
						B.xx=A.xx+1; B.yy=A.yy;
						qu.push(B);
						ar[B.xx][B.yy]=1;
						Cmt++;
					}
					if(A.xx-1>-1&&ar[A.xx-1][A.yy]!=1)
					{
						st B;
						B.xx=A.xx-1; B.yy=A.yy;
						qu.push(B);
						ar[B.xx][B.yy]=1;
						Cmt++;
					}
					qu.pop();
				}
				if(Cmt==0) Cmt=1;
				check[Cnt]=Cmt;
				Cnt++;
			}
		}
	}
	sort(check,check+Cnt);
	printf("%d\n",Cnt);
	for(int x=0; x<Cnt; x++) printf("%d ",check[x]);
}