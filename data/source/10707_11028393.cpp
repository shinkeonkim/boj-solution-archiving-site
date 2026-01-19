#include <iostream>
using namespace std;
int A,B,C,D,P;
int a,b;
int main()
{
    cin>>A>>B>>C>>D>>P;
    a=A*P;
    if(P-C>0)
    {
        b=(P-C)*D+B;
    }
    else b=B;
    cout<< (a>b?b:a);
}