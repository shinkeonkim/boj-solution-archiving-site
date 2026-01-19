#include <iostream>
#include <string>
#include <map>
using namespace std;
int N,M;
string ar[110000];
string Q[110000];
map <string,int> Mp;
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cin.tie(0);
    cin>>N>>M;
    for(int x=1; x<=N; x++)
    {
        cin>>ar[x];
    }
    for(int x=0; x<M; x++) cin>>Q[x];

    for(int x=1; x<=N; x++)
    {
        Mp[ar[x]]=x;
    }

    for(int x=0; x<M; x++)
    {
        if('0'<=Q[x][0]&&Q[x][0]<='9')
        {
            int K=0;
            for(int y=0; y<Q[x].length(); y++)
            {
                K*=10;
                K+=Q[x][y]-'0';
            }
            cout<<ar[K]<<"\n";
        }
        else
        {
            cout<<Mp[Q[x]]<<"\n";
        }
        
    }
}