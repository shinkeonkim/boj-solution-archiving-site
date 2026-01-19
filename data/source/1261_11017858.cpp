#include <iostream>
#include <queue>
#include <cstdio>

#define Mx 99999999
using namespace std;

struct st{
    int Y,X,C;
};

queue <st> que;
st Q;

int N,M,ar[110][110],check[110][110];

int main()
{
    cin>>N>>M;
	for(int y=1; y<=M; y++)
    {
        for(int x=1; x<=N; x++)
        {
        	scanf("%1d",&ar[x][y]);
			check[x][y]=Mx;
        }
    }
    
    check[1][1]=0;
    Q.X=1;
    Q.Y=1;
    Q.C=0;

    que.push(Q);

    while(!que.empty())
    {
        int X=que.front().X;
        int Y=que.front().Y;
        int C=que.front().C;

        if(X>1)
        {
            if(check[X-1][Y]>C+ar[X-1][Y])
            {
                check[X-1][Y]=C+ar[X-1][Y];
                Q.X=X-1;
                Q.Y=Y;
                Q.C=C+ar[X-1][Y];
                que.push(Q);
            }
        }
        
        if(Y>1)
        {
            if(check[X][Y-1]>C+ar[X][Y-1])
            {
                check[X][Y-1]=C+ar[X][Y-1];
                Q.X=X;
                Q.Y=Y-1;
                Q.C=C+ar[X][Y-1];
                que.push(Q);
            }
        }

        if(X<N)
        {
            if(check[X+1][Y]>C+ar[X+1][Y])
            {
                check[X+1][Y]=C+ar[X+1][Y];
                Q.X=X+1;
                Q.Y=Y;
                Q.C=C+ar[X+1][Y];
                que.push(Q);
            }
        }

        if(Y<M)
        {
            if(check[X][Y+1]>C+ar[X][Y+1])
            {
                check[X][Y+1]=C+ar[X][Y+1];
                Q.X=X;
                Q.Y=Y+1;
                Q.C=C+ar[X][Y+1];
                que.push(Q);
            }
        }

        que.pop();
    }
    cout<<check[N][M];
    /*
    cout<<endl;
    for(int y=1; y<=M; y++)
    {
    	for(int x=1; x<=N; x++)
    	{
    		cout<<check[x][y]<<" ";
		}
		cout<<endl;
	}*/
}