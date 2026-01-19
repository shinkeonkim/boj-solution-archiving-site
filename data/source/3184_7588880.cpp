#include <iostream>
#include <queue>
using namespace std;
int a,b,check[300][300],Total1,Total2;
char ar[300][300];
struct st
{
	int X,Y;
};
queue <st> qu;
st Z;
int main()
{
	cin>>a>>b;
	for(int y=0; y<a; y++)
	{
		for(int x=0; x<b; x++)
		{
			cin>>ar[y][x];
			if(ar[y][x]=='#') check[y][x]=1;
		}
	}
	for(int y=0; y<a; y++)
	{
		for(int x=0; x<b; x++)
		{
			if(check[y][x]!=1)
			{
				Z.X=x;Z.Y=y;
				qu.push(Z);
				check[y][x]=1;
			}
			int Cnt1=0,Cnt2=0;
			while(!qu.empty())
			{
				int xx=qu.front().X,yy=qu.front().Y;
				//cout<<xx<<" "<<yy<<endl;
				if(ar[yy][xx]=='o')
				{
					Cnt1++;
				}
				if(ar[yy][xx]=='v')
				{
					Cnt2++;
				}
				if(xx>0)
				{
					if(check[yy][xx-1]!=1)
					{
						Z.X=xx-1;
						Z.Y=yy;
						qu.push(Z);
						check[yy][xx-1]=1;
					}	
				}
				if(yy>0)
				{
					if(check[yy-1][xx]!=1)
					{
						Z.X=xx;
						Z.Y=yy-1;
						qu.push(Z);
						check[yy-1][xx]=1;	
					}
				}
				if(xx<b-1)
				{
					if(check[yy][xx+1]!=1)
					{
						Z.X=xx+1;
						Z.Y=yy;
						qu.push(Z);
						check[yy][xx+1]=1;	
					}	
				}
				if(yy<a-1)
				{
					if(check[yy+1][xx]!=1)
					{
						Z.X=xx;
						Z.Y=yy+1;
						qu.push(Z);
						check[yy+1][xx]=1;	
					}
				}
				qu.pop();
			}
			if(Cnt1>Cnt2) Total1+=Cnt1;
			else Total2+=Cnt2;
		}
	}
	cout<<Total1<<" "<<Total2;
}