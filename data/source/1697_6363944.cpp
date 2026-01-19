#include <iostream>
#include <queue>
using namespace std;
int ar[530000];
struct sss
{
	int x,y;
};
queue <sss> qu;
int CNT;
sss A,B,Z,TMP;
int main()
{
	scanf("%d %d",&A.x,&B.x);
	if(A.x>B.x) printf("%d",(A.x)-(B.x));
	else if(A.x==B.x) printf("0");
	else if(A.x<B.x)
	{
		Z.x=A.x;
		Z.y=0;
		qu.push(Z);
		while(1)
		{
			if(qu.empty())break;
			Z=qu.front();
			TMP.x=Z.x;
			if(Z.x==B.x)
			{
				CNT=Z.y;
				break;
			}
			Z.y++;
			if(Z.x<210000&&ar[Z.x*2]==0)
			{
				ar[Z.x*2]=1;
				Z.x=TMP.x;
				Z.x*=2;
				qu.push(Z);
				//printf("%d ",Z.x);
				Z.x/=2;
			}
			
			if(Z.x-1>0&&ar[Z.x-1]==0)
			{
				ar[Z.x-1]=1;
				Z.x=TMP.x;
				Z.x-=1;
				qu.push(Z);
				//printf("%d ",Z.x);
				Z.x+=1;
			}
			
			if(Z.x<210000&&ar[Z.x+1]==0)
			{
				ar[Z.x+1]=1;
				Z.x=TMP.x;
				Z.x+=1;
				qu.push(Z);
				//printf("%d ",Z.x);
				Z.x-=1;
			}
			qu.pop();
		}
		printf("%d",CNT);
	}
}