#include <iostream>
using namespace std;
int N,S=1,K=1;
int main()
{
    cin>>N;
    while(S<N)
    {
        S+=K*6;
        K++;
        if(S>=N)
        {
            cout<<K;
            return 0;
        }
    }
    cout<<1;
}
