#include <iostream>
using namespace std;
int N,R,W,ar[55];
int main()
{
    cin>>N>>R>>W;
    for(int x=0; x<N; x++) cin>>ar[x];
    for(int x=0; x<N; x++)
    {
        if(ar[x]*ar[x]<=R*R+W*W) cout<<"DA\n";
        else cout<<"NE\n";
    }
}