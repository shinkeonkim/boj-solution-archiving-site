#include <bits/stdc++.h>
using namespace std;
struct st{
    unsigned long long X,Y,V,D,T;
};

int N;
st ar[220000];

bool compare(st a,st b)
{
    if(a.D*b.V*b.V < a.V*a.V*b.D) return true;
    else if(a.D*b.V*b.V == a.V*a.V*b.D)
    {
        if(a.T<b.T) return true;
    }
    return false;
}

int main()
{
    cin>>N;
    for(int x=0; x<N; x++) cin>>ar[x].X>>ar[x].Y>>ar[x].V;
    for(int x=0; x<N; x++)
    {
        ar[x].T = x+1;
        ar[x].D=(ar[x].X*ar[x].X) + (ar[x].Y*ar[x].Y);
    }
    sort(ar,ar+N,compare);
    for(int x=0; x<N; x++) cout<<ar[x].T<<"\n";
}