#include <iostream>
using namespace std;
int N,ar[110],A;
int main()
{
    while(true)
    {
        cin>>N;
        if(N==0) return 0;
        for(int x=0; x<N; x++)
        {
            cin>>ar[x];
        }
        cout<<ar[0]<<" ";
        for(int x=1; x<N; x++)
        {
            if(ar[x]!=ar[x-1]) cout<<ar[x]<<" ";
        }
        cout<<"$\n";
    }
}