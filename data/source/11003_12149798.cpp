#include <iostream>
#include <queue>
using namespace std;
struct st{
    int A,C; //A는 몇번째, C는 수치 
};
struct compare{
    bool operator()(st a, st b)
    {
        return a.C>b.C;
    }
};
priority_queue <st,vector<st>,compare> Q;
int N,L,ar[5500000];
st Z;
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    cin>>N>>L;
    for(int x=1; x<=N; x++)
    {
        cin>>ar[x];
    }
    for(int x=1; x<=N; x++)
    {
        Z.A=x;
        Z.C=ar[x];
        Q.push(Z);
        while(!(x-L+1<=Q.top().A&&Q.top().A<=x))
        {
            Q.pop();
        }
        cout<<Q.top().C<<" ";
    }

}