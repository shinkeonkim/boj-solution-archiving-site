#include <iostream>
using namespace std;
long long ar[88],S;
int N;
int main()
{
    cin>>N;
    ar[1]=ar[2]=1;
    for(int x=3; x<=N; x++)
    {
        ar[x]=ar[x-1]+ar[x-2];
    }
    S=ar[N]*4+ar[N-1]*2;
    cout<<S;
}