#include <iostream>
#include <cstdio>
using namespace std;
int N,M,Cnt;
int A[55][55],B[55][55];
int main()
{
    cin>>N>>M;
    for(int y=0; y<N; y++)
    {
        for(int x=0; x<M; x++)
        {
            scanf("%1d",&A[y][x]);
        }
    }

    for(int y=0; y<N; y++)
    {
        for(int x=0; x<M; x++)
        {
            scanf("%1d",&B[y][x]);
        }

    }
    for(int y=0; y<N-2; y++)
    {
        for(int x=0; x<M-2; x++)
        {
            if(A[y][x]!=B[y][x])
            {
                Cnt++;
                for(int Y=0; Y<3; Y++)
                {
                    for(int X=0; X<3; X++)
                    {
                        A[y+Y][x+X]=1-A[y+Y][x+X];
                    }
                }
            }
        }
    }

    for(int y=0; y<N; y++)
    {
        for(int x=0; x<M; x++)
        {
            if(A[y][x]!=B[y][x])
            {
                cout<<-1;
                return 0;
            }
        }
    }
    cout<<Cnt;
}