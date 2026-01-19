#include <bits/stdc++.h>
using namespace std;
int N,M;
int ar[330][330],D[330][330];
int main()
{
    cin>>N>>M;
    for(int y=1; y<=N; y++)
    {
        for(int x=1; x<=M; x++)
        {
            cin>>ar[y][x];
        }
    }
    for(int y=1; y<=N; y++)
    {
        for(int x=1; x<=M; x++)
        {
            D[y][x]= ar[y][x] + max(D[y-1][x],D[y][x-1]);
        }
    }
    cout<<D[N][M];
}