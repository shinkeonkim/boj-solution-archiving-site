#include <iostream>
using namespace std;
int a,S1,S2;
int main()
{
    for(int x=3; x>=1; x--)
    {
        cin>>a;
        S1+=a*x;
    }
    for(int x=3; x>=1; x--)
    {
        cin>>a;
        S2+=a*x;
    }
    if(S1==S2) cout<<"T";
    else if(S1>S2) cout<<"A";
    else cout<<"B";
}