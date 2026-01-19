#include <iostream>
using namespace std;
int N;
int K,S,check[110000];
int main()
{
    cin>>N;
    if(N==1)
    {
        cout<<"HAPPY";
        return 0;
    }
    K=N;
    while(1)
    {
        S=0;
        while(K>0)
        {
            S+=(K%10)*(K%10);
            K/=10;
        }
        if(S==1)
        {
            cout<<"HAPPY";
            return 0;
        }
        if(check[S]==1)
        {
            cout<<"UNHAPPY";
            return 0;
        }
        check[S]=1;
        K=S;
    }
}