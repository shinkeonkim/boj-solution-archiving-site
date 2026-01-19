#include <iostream>
using namespace std;
int N,T,ar[550],S=0;
int main()
{
    cin>>N>>T;
    for(int x=0; x<N; x++) cin>>ar[x];
    for(int x=0; x<N; x++)
    {
        S+=ar[x];
        if(S>T)
        {
            cout<<x;
            return 0;
        }
        else if(S==T)
        {
            cout<<x+1;
            return 0;   
        }
    }
    cout<<N;
}