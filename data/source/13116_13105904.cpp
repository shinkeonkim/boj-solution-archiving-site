#include <iostream>
using namespace std;
int N,a,b;
int main()
{
    cin>>N;
    for(int x=0; x<N; x++)
    {
        cin>>a>>b;
        while(a!=b)
        {
            if(a>b) a/=2;
            else if(a<b) b/=2;
        }
        cout<<a<<"0\n";
        
    }
}