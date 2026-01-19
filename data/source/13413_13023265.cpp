#include <iostream>
#include <algorithm>
using namespace std;
int Cnta,Cntb;
int T,N;
string a,b;
int main()
{
    cin>>T;
    for(int t=0; t<T; t++)
    {
        cin>>N>>a>>b;
        Cnta=Cntb=0;
        for(int x=0; x<N; x++)
        {
            if(a[x]=='W' && b[x] == 'B') Cnta++;
            if(a[x]=='B' && b[x] == 'W') Cntb++;
        }
        cout<<Cnta+Cntb-min(Cnta,Cntb)<<"\n";
    }
}