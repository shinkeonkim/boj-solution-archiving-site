#include <iostream>
using namespace std;
int N,a,b,ar[11000],Cnt;
int main()
{
    cin>>N;
    for(int x=0; x<N; x++)
    {
        cin>>a>>b;
        for(int y=a; y<b; y++) ar[y]=1;
    }

    for(int x=1; x<=10000; x++) if(ar[x]==1) Cnt++;
    
    cout<<Cnt;
}