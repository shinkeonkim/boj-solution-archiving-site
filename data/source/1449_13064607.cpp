#include <iostream>
#include <algorithm>
using namespace std;
int N,L,S,Z,ar[1100];
int main()
{
    cin>>N>>L;
    for(int x=0; x<N; x++) cin>>ar[x];
    sort(ar,ar+N);
    S++;
    Z=ar[0];
    for(int x=1; x<N; x++)
    {
        if(L<=ar[x]-Z)
        {
            S++;
            Z=ar[x];
        }
    }
    cout<<S;
}