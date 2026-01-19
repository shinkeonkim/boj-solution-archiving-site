#include <iostream>
using namespace std;
int a,x,y,s,ar[101][101];
int main()
{
    cin>>a;
    for(int q=0; q<a; q++)
    {
        cin>>x>>y;
        for(int w=x; w<x+10; w++)
        {
            for(int e=y; e<y+10; e++)
            {
                ar[w][e]=1;
            }
        }
    }
    for(int x=0; x<101; x++)
    {
        for(int y=0; y<101; y++)
        {
            s+=ar[x][y];
        }
    }
    cout<<s;
}