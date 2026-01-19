#include <iostream>
#include <string>
using namespace std;
int Y,X,Max;
int dy[]={0,0,1,-1};
int dx[]={1,-1,0,0};
string ar[55];
int check[55],M[22][22];
void f(int a, int b, int c)
{
	if(c>Max) Max=c;
	for(int d=0; d<4; d++)
	{
		if(0<=a+dy[d]&&a+dy[d]<Y && 0<=b+dx[d] && b+dx[d]<X)
		{
			if(check[ar[a+dy[d]][b+dx[d]]-'A']!=1/*&&M[a+dy[d]][b+dx[d]]<c+1*/)
			{
				//M[a+dy[d]][b+dx[d]]=c+1;
				check[ar[a+dy[d]][b+dx[d]]-'A']=1;
				f(a+dy[d],b+dx[d],c+1);
				check[ar[a+dy[d]][b+dx[d]]-'A']=0;
			}
		}
	}
	
}
int main()
{
	cin>>Y>>X;
	for(int y=0; y<Y; y++) {
		cin>>ar[y];
	}
	M[0][0]=1;
	check[ar[0][0]-'A']=1;
	f(0,0,1);
	cout<<Max;
}