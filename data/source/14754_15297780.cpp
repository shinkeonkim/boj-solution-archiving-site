#include <iostream>
#define ll long long
using namespace std;
ll N,M,S;
ll ar[1100][1100];
ll D[1100][1100],Pos,Max;
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
        Pos=0;
        Max=ar[y][0];
        for(int x=1; x<M; x++)
        {
            if(Max<ar[y][x])
            {
                Max=ar[y][x];
                Pos=x;
            }
        }
        D[y][Pos]=1;
    }

    for(int x=0; x<M; x++)
    {
        Pos=0;
        Max=ar[0][x];
        for(int y=1; y<N; y++)
        {
            if(Max<=ar[y][x])
            {
                Max=ar[y][x];
                Pos=y;
            }
        }
        D[Pos][x]=1;
    }

    for(int y=0; y<N; y++)
    {
        for(int x=0; x<M; x++)
        {
            if(!D[y][x]) S+=ar[y][x];
        }
    }
    cout<<S;

}