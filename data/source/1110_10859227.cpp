#include <iostream>
using namespace std;
int N,Cnt=1,A;
int main()
{
    cin>>N;
    A=((N/10+N%10)%10)+(N%10)*10;
    while(A!=N)
    {
        A=((A/10+A%10)%10)+(A%10)*10;
        Cnt++;
    }
    cout<<Cnt;
}

