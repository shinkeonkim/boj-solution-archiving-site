#include <iostream>
using namespace std;
int N,M,K,X,Y;
int D[20][20];
int C(int n,int r)
{
    if(n<0||r<0) return 0;
    else if(D[n][r]) return D[n][r];
    else if(n<r) return D[n][r]=0;
    else if(n==r) return D[n][r]=1;
    else if(r==1) return D[n][r]=n;
    else return D[n][r]=C(n-1,r)+C(n-1,r-1); 
}
int main()
{
    cin>>N>>M>>K;

    if(K==0)
    {
        cout<<C(N+M-2,N-1);
        return 0;
    }
    X=K%M;
    Y=K/M;
    if(K%M==0) 
    {
        Y--;
        X=M;
    }
    X--;
    cout<<C(X+Y,X)*C(N+M-(X+Y+2),(N-Y-1));
}