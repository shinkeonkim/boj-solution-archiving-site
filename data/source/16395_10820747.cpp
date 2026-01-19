#include <iostream>

using namespace std;
int N,K;
int ar[44][44];
int f(int n,int r)
{
    if(ar[n][r]) return ar[n][r];
    else if(n==0||r==0) return ar[n][r]=1;
    else if(n<r) return ar[n][r]=0;
    else if(n==r) return ar[n][r]=1;
    else if(r==1) return ar[n][r]=n;
    else return ar[n][r]=f(n-1,r-1)+f(n-1,r);
}
int main()
{
    cin>>N>>K;
    cout<<f(N-1,K-1);
}