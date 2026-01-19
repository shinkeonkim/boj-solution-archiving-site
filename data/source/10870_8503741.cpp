#include <iostream>
using namespace std;
int ar[100]={0,1},N;
int main()
{
    cin>>N;
    if(N==0||N==1)cout<<ar[N];
    else 
    {
        for(int x=2; x<=N; x++) ar[x]=ar[x-1]+ar[x-2];
        cout<<ar[N];
    }
}