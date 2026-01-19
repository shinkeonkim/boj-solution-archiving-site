#include <iostream>
using namespace std;
unsigned long long N;
unsigned long long D[1100][1100];
unsigned long long f(unsigned long long a,unsigned long long b)
{
    if(D[a][b]) return D[a][b];
    else if(a<b) return D[a][b]=0;
    else if(b==1) return D[a][b]=a;
    else if(a==b) return D[a][b]=1;
    else return D[a][b]=f(a-1,b-1)+f(a-1,b);
}
int main()
{
    cin>>N;cout<<f(N/3-1,2);
}