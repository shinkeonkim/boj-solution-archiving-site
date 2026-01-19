#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int N,T;
int D[9900000];
vector <int> V;
int main()
{
    ios_base :: sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    
    for(int x=2; x<=1000000; x++)
    {
        D[x]=x;
    }
    for(int x=2; x<=1000000; x++)
    {
        if(D[x]==x)
        {
            V.push_back(x);
            for(int y=x+x; y<=1000000; y+=x)
            {
                D[y]=0;
            }
        }
    }
    while(1)
    {
        cin>>N;
        if(N==0) break;
        for(int k=0; k<V.size() && V[k]<= N/2; k++)
        {
            if(D[N-V[k]]==N-V[k])
            {
                cout<<N<<" = "<<V[k]<<" + "<<N-V[k]<<"\n";
                break;
            }
        }
    }   
}