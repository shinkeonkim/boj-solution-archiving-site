#include <iostream>
using namespace std;
long long int N,T,A,S;
int main ()
{
    cin>>T;
    for(int i=0; i<T; i++)
    {
        S=0;
        cin>>N;
        for(int z=0; z<N;z++)
        {
            cin>>A;
            S+=A;
        }
        cout<<S<<endl;
    }
}