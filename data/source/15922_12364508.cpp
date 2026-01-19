#include <bits/stdc++.h>
#include <stack>
using namespace std;
struct st{
    long long A,B;
};

st ar[110000];
long long N,S;
stack <st> stk;
st K;
int main()
{
    cin>>N;
    for(int x=0; x<N; x++) cin>>ar[x].A>>ar[x].B;
    stk.push(ar[0]);   
    for(int x=1; x<N; x++)
    {
        K=stk.top();
        stk.pop();
        if(ar[x].A<=K.B && ar[x].B >= K.B)
        {
            K.B=ar[x].B;
            stk.push(K);
        }
        else if(ar[x].A<=K.B &&  ar[x].B < K.B) 
        {
            stk.push(K);
        }
        else
        {
            stk.push(K);
            stk.push(ar[x]);
        }
    }
    while(!stk.empty())
    {
        S+=stk.top().B-stk.top().A;
        stk.pop();
    }
    cout<<S;

}