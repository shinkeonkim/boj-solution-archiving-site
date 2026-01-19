#include <bits/stdc++.h>
using namespace std;
struct st{
    int Y,M,D;
    string name;
};
st ar[110];
int N;

bool compare(st a,st b)
{
    if(a.Y<b.Y) return true;
    else if(a.Y==b.Y)
    {
        if(a.M<b.M) return true;
        else if(a.M==b.M)
        {
            if(a.D<b.D) return true;
        }
    }
    return false;
}

int main()
{
    cin>>N;
    for(int x=0; x<N; x++)
    {
        cin>>ar[x].name>>ar[x].D>>ar[x].M>>ar[x].Y;
    }
    sort(ar,ar+N,compare);
    cout<<ar[N-1].name<<endl<<ar[0].name;
}