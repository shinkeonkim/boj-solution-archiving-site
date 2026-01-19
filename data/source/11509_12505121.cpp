#include <iostream>
using namespace std;
int N,S;
int H[1100000];
int D[1100000];
int main()
{
    cin>>N;
    for(int x=0; x<N; x++)
    {
        cin>>H[x];
    }
    for(int x=0; x<N; x++)
    {
        if(D[H[x]]>0)
        {
            D[H[x]]--;
            if(H[x]-1>0) D[H[x]-1]++;
        }
        else
        {
            S++;
            if(H[x]-1>0) D[H[x]-1]++;
        }
    }
    cout<<S;
}