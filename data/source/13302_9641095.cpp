#include <iostream>
#include <algorithm>
#define Mx 999999999
using namespace std;
int N,M,ar[220],A,D[220][110],ans=Mx;
int main()
{
    cin>>N>>M;
    for(int x=0; x<M; x++)
    {
        cin>>A;
        ar[A]=1;
    }
     
    for(int x=0; x<=N; x++)
    {
        for(int y=0; y<50; y++) D[x][y]=Mx;
    }
     
    D[0][0]=0;
     
    for(int x=0; x<=N; x++)
    {
        for(int y=0; y<50; y++)
        {
            if(D[x][y]!=Mx)
            {
                if(ar[x+1]==1)
                {
                    D[x+1][y]=D[x][y];
                }
                else
                {
                    D[x+1][y]=min(D[x+1][y],D[x][y]+10);
                    for(int i=1; i<=3; i++)
                    {
                        D[x+i][y+1]=min(D[x+i][y+1],D[x][y]+25);
                    }   
                    for(int i=1; i<=5; i++)
                    {
                        D[x+i][y+2]=min(D[x+i][y+2],D[x][y]+37);
                    }
                    if(y>2)
                    {
                        D[x+1][y-3]=min(D[x+1][y-3],D[x][y]);
                    }
                }
            }
        }
    }
    for(int x=0; x<50; x++)
    {
        ans=min(ans,D[N][x]);
    }
    cout<<ans*1000;
     
     
    /*cout<<endl<<endl;
    for(int y=0; y<=5; y++)
    {
        for(int x=0; x<=N; x++)
        {
            if(D[x][y]!=Mx) cout<<D[x][y]<<" ";
            else cout<<"**"<<" ";
        }
        cout<<endl;
    }*/
     
}