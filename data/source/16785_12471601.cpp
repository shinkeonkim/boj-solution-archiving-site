#include <iostream>
using namespace std;
int A,B,C,S,K;
int main()
{
    cin>>A>>B>>C;
    while(S<C)
    {
        K++;
        S+=A;
        if(K!=0&&K%7==0)
        {
            S+=B;
        }
    }
    cout<<K;
}