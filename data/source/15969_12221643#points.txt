#include <iostream>
using namespace std;
int N,A,Min=9001,Max=-1;
int main()
{
    cin>>N;
    for(int x=0; x<N; x++)
    {
        cin>>A;
        if(A>Max) Max=A;
        if(A<Min) Min=A;
    }
    cout<<Max-Min;
}