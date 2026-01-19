#include <iostream>
using namespace std;
int N;
int main()
{
    cin>>N;
    if(N==1)
    {
        cout<<1;
        return 0;
    }
    while(N>2)
    {
        if(N%2==0) N/=2;
        else
        {
            cout<<0;
            return 0;
        }
    }
    if(N==2) cout<<1;
    else cout<<0;
}