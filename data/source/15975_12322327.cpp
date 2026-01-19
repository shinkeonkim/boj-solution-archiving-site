#include <iostream>
#include <algorithm>
using namespace std;
struct st{
    long long X,Color;
};
long long N,S;
st ar[110000];

bool compare(st a, st b)
{
    if(a.Color<b.Color) return true;
    else if(a.Color==b.Color)
    {
        if(a.X<b.X)
        {
            return true;
        }
    }
    return false;
}
int main()
{
    cin>>N;
    for(int x=0; x<N; x++) cin>>ar[x].X>>ar[x].Color;
    sort(ar,ar+N,compare);
    for(int x=0; x<N; x++)
    {
        if(x==0)
        {
            if(ar[x+1].Color==ar[x].Color)
            {
                S+=ar[x+1].X-ar[x].X;
            }
        }
        else
        {
            long long M=999999999999;
            if(ar[x+1].Color==ar[x].Color)
            {
                if(ar[x+1].X-ar[x].X<M) M=ar[x+1].X-ar[x].X;
            }
            if(ar[x-1].Color==ar[x].Color)
            {
                if(ar[x].X-ar[x-1].X<M) M=ar[x].X-ar[x-1].X;
            }
            if(M!=999999999999) S+=M;
        }
        
    }
    cout<<S;
}