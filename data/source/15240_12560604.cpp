#include <iostream>
#include <cstdio>
using namespace std;
int R,C,Y,X,K,A;
int dy[]={0,0,1,-1},dx[]={1,-1,0,0};
int ar[1100][1100];

void DFS(int y,int x)
{
    ar[y][x]=K;
    for(int d=0; d<4; d++)
    {
        int ny=y+dy[d];
        int nx=x+dx[d];
        if(ny<0 || ny >= R || nx<0 || nx >= C) continue;

        if(ar[ny][nx]==A)
        {
            DFS(ny,nx);
        }
    }
}
int main()
{
    cin>>R>>C;
    for(int y=0; y<R; y++)
    {
        for(int x=0; x<C; x++) scanf("%1d",&ar[y][x]);
    }
    cin>>Y>>X>>K;
    if(ar[Y][X]!=K)
    {
        A=ar[Y][X];
        DFS(Y,X);
    }
    for(int y=0; y<R; y++)
    {
        for(int x=0; x<C; x++)
        {
            cout<<ar[y][x];
        }
        cout<<endl;
    }
}   