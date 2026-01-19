#include <iostream>
using namespace std;
char ar[20][10];
int check[20][10],Cnt,total=1,totalCnt; //12*6;

void DFS(int y,int x,char a)
{
	Cnt++;
	check[y][x]=1;
	if(x>0)
	{
		if(ar[y][x-1]==a&&check[y][x-1]==0)
		{
			DFS(y,x-1,a);
		}
	}
	if(y>0)
	{
		if(ar[y-1][x]==a&&check[y-1][x]==0)
		{
			DFS(y-1,x,a);
		}
	}
	if(y<11)
	{
		if(ar[y+1][x]==a&&check[y+1][x]==0)
		{
			DFS(y+1,x,a);
		}
	}
	if(x<11)
	{
		if(ar[y][x+1]==a&&check[y][x+1]==0)
		{
			DFS(y,x+1,a);
		}
	}
}

void erasecheck()
{
	for(int y=0; y<12; y++)
		for(int x=0; x<6; x++)
		{
			if(check[y][x]==1)
			{
				ar[y][x]='.';
			}
		}
}
void change1check()
{
	for(int y=0; y<12; y++)
		for(int x=0; x<6; x++)
		{
			if(check[y][x]==1)
			{
				check[y][x]=2;
			}
		}
}

void change2check()
{
	for(int y=0; y<12; y++)
		for(int x=0; x<6; x++)
		{
			check[y][x]=0;
		}
}

void Down()
{
	for(int y=10; y>-1; y--)
	{
		for(int x=0; x<6; x++)
		{
			if(ar[y][x]!='.')
			{
				int Y=y;
				for(int y2=y+1; y2<12; y2++)
				{
					if(ar[y2][x]=='.') Y=y2;
					else break; 
				}
				ar[Y][x]=ar[y][x];
				if(Y!=y)ar[y][x]='.';
				//cout<<x<<" "<<y<<"-> "<<Y<<endl;
			}
			
		}
	}
}

int main()
{
	for(int y=0; y<12; y++)
	{
		for(int x=0; x<6; x++) cin>>ar[y][x];
	}
	
	while(total!=0)
	{
		total=0;
		Cnt=0;
		for(int y=0; y<12; y++)
		{
			for(int x=0; x<6; x++)
			{
				if(ar[y][x]!='.'&&check[y][x]==0)
				{
					Cnt=0;
					DFS(y,x,ar[y][x]);
					if(Cnt>3)
					{
						total++;
						erasecheck(); //1로 check된 좌표 .으로 바꾸기 
					}
					else
					{
						change1check();// 1로 check된 얘 2로 바꾸기 
					}
				}
			}
		}
		change2check();
		if(total>0) totalCnt++;
		Down();
		/*
		for(int y=0; y<12; y++)
		{
			for(int x=0; x<6; x++)
			{
				cout<<ar[y][x];
			}
			cout<<endl;
		}
		cout<<endl;*/
	}
	cout<<totalCnt;
}