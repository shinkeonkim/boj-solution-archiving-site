#include <bits/stdc++.h>
using namespace std;
int N,A;
vector <int> V;
int main()
{
    cin>>N;
    for(int x=0; x<N; x++)
    {
        cin>>A;
        V.push_back(A);
    }
    if(next_permutation(V.begin(),V.end()))
    {
        for(int x=0; x<V.size(); x++) cout<<V[x]<<" ";
    }
    else
    {
        cout<<-1;
    }
    
}