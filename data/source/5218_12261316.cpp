#include <iostream>
#include <string>
using namespace std;
int N;
string ar[110][2];
int f(int a,int b)
{
    if(b>=a) return b-a;
    else return (b+26)-a;
}
int main()
{
    cin>>N;
    for(int y=0; y<N; y++)
    {
        for(int x=0; x<2; x++) cin>>ar[y][x];
    }

    for(int y=0; y<N; y++)
    {   
        cout<<"Distances: ";
        for(int x=0; x<ar[y][0].length(); x++)
        {
            cout<<f(ar[y][0][x],ar[y][1][x])<<" ";
        }
        cout<<endl;
    }
}