#include <iostream>
using namespace std;

long long T,N,M,ans,ar[550000];

long long gcd(long long A,long long B)
{
    return B>0?gcd(B,A%B):A;
}

int main()
{
    cin>>T;
    for(int t=0; t<T; t++) cin>>ar[t];
    for(int t=0; t<T; t++)
    {
        ans=0;
        N=ar[t];
        if(N==1)
        {
            cout<<1<<endl;
            continue;
        }
        for(long long x=1; x*x<N; x++)
        {
            if(N%x==0 && gcd(x,N/x)==1 )
            {
                ans++;
            }
        }
        cout<<ans<<endl;
    }
}