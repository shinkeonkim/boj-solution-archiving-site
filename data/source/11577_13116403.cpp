#include <iostream>
using namespace std;
int N,K,Cnt,tCnt;
int ar[110000];
int D[220000];
int main()
{
    cin>>N>>K;
    for(int x=0; x<N; x++) cin>>ar[x];
    for(int x=0; x<N; x++)
    {
        Cnt-=D[x];
        if((ar[x]+Cnt)%2==1&&x+K<=N)
        {
            ar[x]=0;
            tCnt++;
            Cnt++;
            D[x+K]++;
        }
        else if((ar[x]+Cnt)%2==1)
        {
            ar[x]=1;
        }
        else if((ar[x]+Cnt)%2==0)
        {
            ar[x]=0;
        }
    }
    for(int x=0; x<N; x++)
    {
        if(ar[x]==1)
        {
            cout<<"Insomnia";
            return 0;
        }
    }
    cout<<tCnt;
}