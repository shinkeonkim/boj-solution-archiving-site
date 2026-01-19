#include <bits/stdc++.h>
using namespace std;
int N,L;
int ar[1100];
int main()
{
    cin>>N>>L;
    for(int x=0; x<N; x++) cin>>ar[x];
    sort(ar,ar+N);
    for(int x=0; x<N; x++)
    {
        if(ar[x]<=L) L++;
    }
    cout<<L;
}