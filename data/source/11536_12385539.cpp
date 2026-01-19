#include <bits/stdc++.h>
using namespace std;
int N,S;
string ar[22];
int main()
{
    cin>>N;
    for(int x=0; x<N; x++) cin>>ar[x];
    for(int x=0; x<N-1; x++)
    {
        if(ar[x].compare(ar[x+1])>0) S+=1;
        else S+=2;
    }
    if(S==N-1) cout<<"DECREASING";
    else if(S==2*(N-1)) cout<<"INCREASING";
    else cout<<"NEITHER";
}