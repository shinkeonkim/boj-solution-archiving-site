#include <iostream>
#include <queue>
#include <cstdio>
#include <algorithm>
#define Mx 987654321
using namespace std;

struct st{
    int Y,X,C,D;
};

int K,ans,N,M,ar[1100][1100],D[1100][1100][11];
int dy[]={0,0,1,-1};
int dx[]={1,-1,0,0};
st Q;
queue <st> que;
int main()
{
    cin>>N>>M>>K;
    for(int y=0; y<N; y++)
    {
        for(int x=0; x<M; x++) scanf("%1d",&ar[y][x]);
    }

    for(int y=0; y<N; y++)
    {
        for(int x=0; x<M; x++)
        {
            for(int z=0; z<=K; z++) D[y][x][z]=Mx;
        }   
    }

    Q.Y=0;
    Q.X=0;
    Q.D=1;
    Q.C=ar[0][0];
    D[0][0][ar[0][0]]=1;

    que.push(Q);
    while(!que.empty())
    {
        st Z;
        Z=que.front();
        que.pop();
        for(int d=0; d<4; d++)
        {
            int next_X=Z.X+dx[d];
            int next_Y=Z.Y+dy[d];

            if(0<=next_X && next_X<M && 0<=next_Y && next_Y<N)
            {
                if(ar[next_Y][next_X]==1 && Z.C<K)
                {
                    if(Z.D%2==1)
                    {
                        if(D[next_Y][next_X][Z.C]>Z.D+1)
                        {
                            D[next_Y][next_X][Z.C]=Z.D+1;
                            Q.X=next_X;
                            Q.Y=next_Y;
                            Q.C=Z.C+1;
                            Q.D=Z.D+1;
                            que.push(Q);    
                        }
                    }   
                    else
                    {
                        if(D[next_Y][next_X][Z.C]>Z.D+2)
                        {
                            D[next_Y][next_X][Z.C]=Z.D+2;
                            Q.X=next_X;
                            Q.Y=next_Y;
                            Q.C=Z.C+1;
                            Q.D=Z.D+2;
                            que.push(Q);
                        }
                    }
                }
                else if(ar[next_Y][next_X]==0)
                {
                    if(D[next_Y][next_X][Z.C]>Z.D+1)
                    {       
                        D[next_Y][next_X][Z.C]=Z.D+1;
                        Q.X=next_X;
                        Q.Y=next_Y;
                        Q.C=Z.C;
                        Q.D=Z.D+1;
                        que.push(Q);
                    }
                }
            }
        }
    }
    ans=D[N-1][M-1][0];
    for(int x=1; x<=K; x++)
    {
        ans = min(ans,D[N-1][M-1][x]);
    }
    if(ans==Mx) cout<<-1;
    else cout<<ans;
}