#include <bits/stdc++.h>
using namespace std;
int T,W;
int D[1100][33][3];
int ar[1100];
int main()
{
    cin>>T>>W;
    for(int x=0; x<T; x++)
    {
        cin>>ar[x];
    }
    if(W>0)
    {
        if(ar[0]==2) D[0][1][2]=1;
    }
    if(ar[0]==1) D[0][0][1]=1;

    for(int t=1; t<T; t++)
    {
        for(int w=0; w<=W; w++)
        {
            for(int z=1; z<3; z++)
            {
                for(int k=1; k<3; k++)
                {
                    if(k!=z && w+1<=W)
                    {
                        D[t][w+1][z]=max(D[t][w+1][z],D[t-1][w][k]+ (ar[t]==z?1:0));
                    }
                    if(k==z)
                    {
                        D[t][w][z]=max(D[t][w][z],D[t-1][w][z]+(ar[t]==z?1:0));
                    }
                }
            }
        }
    }
    int Max=0;
    for(int w=0; w<=W; w++)
    {
        for(int z=1; z<3; z++)
        {
            Max=max(Max,D[T-1][w][z]);
        }
    }
    cout<<Max;
}