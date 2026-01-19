#include <bits/stdc++.h>
using namespace std;
int N;
int ar[1100000];
vector <int> V;
int main()
{
    cin>>N;
    for(int x=0; x<N; x++) cin>>ar[x];
    V.push_back(ar[0]);
    for(int x=1; x<N; x++)
    {
        if(V.back()<ar[x])
        {
            V.push_back(ar[x]);
        }
        else
        {
            auto iter = lower_bound(V.begin(),V.end(),ar[x]);
            *iter = ar[x];   
        }
    }
    cout<<V.size();
}