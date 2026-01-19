#include <bits/stdc++.h>
using namespace std;
int N,M;
int ar[1100][1100];
int D[1100][1100];
int main()
{
    cin>>N>>M;
    for(int y=0; y<N; y++)
    {
        for(int x=0; x<M; x++)
        {
            cin>>ar[y][x];
        }
    }

    for(int y=0; y<N; y++)
    {
        for(int x=0; x<M; x++)
        {
            if(y==0&&x==0)
            {
                D[y][x]=ar[y][x];
            }
            else if(y==0)
            {
                D[y][x]=D[y][x-1]+ar[y][x];
            }
            else if(x==0)
            {
                D[y][x]=D[y-1][x]+ar[y][x];
            }
            else
            {
                D[y][x]=max(D[y-1][x],D[y][x-1])+ar[y][x];
            }
            
        }
    }

    cout<<D[N-1][M-1];

}