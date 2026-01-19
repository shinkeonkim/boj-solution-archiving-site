#include <iostream>
#include <queue>
#define Mx 97654321
using namespace std;

struct st{
    int Z,Y,X,T;
};

int L,R,C; // L은 빌딩의 층수, R은 빌딩의 행, C는 빌딩의 열
char ar[44][44][44],buf; //빌딩의 정보
int D[44][44][44]; //출발지점부터 각 칸까지 이동할 때의 최소 시간
int Sx,Sy,Sz,Ex,Ey,Ez;
int next_Z,next_Y,next_X;
int dz[]={0,0,0,0,1,-1};
int dy[]={0,0,1,-1,0,0};
int dx[]={1,-1,0,0,0,0};

queue <st> que;
st Q;

int main()
{    
    ios_base::sync_with_stdio(true);
    cin.tie(0);
    cout.tie(0);
    while(1)
    {
        cin>>L>>R>>C;
        if(L==0&&R==0&&C==0) return 0;

        for(int z=0; z<L; z++)
        {
            for(int y=0; y<R; y++)
            {
                for(int x=0; x<C; x++)
                {
                    cin>>ar[z][y][x];
                    D[z][y][x]=Mx;
                    if(ar[z][y][x]=='S')
                    {
                        Sz=z;
                        Sy=y;
                        Sx=x;
                        D[z][y][x]=0;
                    }
                    if(ar[z][y][x]=='E')
                    {
                        Ez=z;
                        Ey=y;
                        Ex=x;
                    }
                }
            }
        }

        que.push({Sz,Sy,Sx,0});
        while(!que.empty())
        {
            st Z=que.front();
            que.pop();
            for(int d=0; d<6; d++)
            {
                next_Z=Z.Z+dz[d];
                next_Y=Z.Y+dy[d];
                next_X=Z.X+dx[d];

                if(next_Z < 0  || next_Y < 0 || next_X < 0 || next_Z >= L || next_Y >=R || next_X >= C) continue;

                if(ar[next_Z][next_Y][next_X]!='#' && D[next_Z][next_Y][next_X]>Z.T+1)
                {
                    D[next_Z][next_Y][next_X]=Z.T+1;
                    Q.Z=next_Z;
                    Q.Y=next_Y;
                    Q.X=next_X;
                    Q.T=Z.T+1;
                    que.push(Q);
                }

            }
        }
        if(D[Ez][Ey][Ex]==Mx) cout<<"Trapped!\n";
        else cout<<"Escaped in "<<D[Ez][Ey][Ex]<<" minute(s).\n";
    }
}