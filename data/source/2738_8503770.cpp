#include <iostream>
using namespace std;
int ar[110][110],N,M,a;
int main()
{
    cin>>N>>M;
    for(int z=0; z<2; z++)
    {
        for(int x=0; x<N; x++)
        {
           for(int y=0; y<M; y++)
           {
               cin>>a;
               ar[x][y]+=a;
           }
        }
    }
    for(int x=0; x<N; x++)
    {
        for(int y=0; y<M; y++)
        {
            cout<<ar[x][y]<<" ";
        }
        cout<<endl;
    }
        
}