#include <iostream>
using namespace std;
int N,A,B,a,b;
int main()
{
    cin>>N;
    for(int x=0; x<N; x++)
    {
        cin>>a>>b;
        if(a>b) A++;
        if(a<b) B++;
    }
    cout<<A<<" "<<B;
}
