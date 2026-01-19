#include <iostream>
using namespace std;
int a,b,ar[22];
void f(int a,int b)
{
    if(a>b) return ;
    else
    {
        int tmp=ar[b];
        ar[b]=ar[a];
        ar[a]=tmp;
        f(a+1,b-1);
    }
}
int main()
{
    for(int x=1; x<=20; x++)ar[x]=x;
    for(int x=0; x<10; x++)
    {
        cin>>a>>b;
        f(a,b);
    }
    for(int x=1; x<=20; x++)cout<<ar[x]<<" ";
}