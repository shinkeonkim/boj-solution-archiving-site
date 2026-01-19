#include <iostream>
using namespace std;
int N,K,T,A,Max=-1;
int main()
{
    cin>>N>>K;
    for(int x=1; x<=K; x++)
    {
        T=N*x;
        A=0;
        while(T>0)
        {
            A*=10;
            A+=T%10;
            T/=10;
        }
        if(A>Max) Max=A;
    }
    cout<<Max;
}