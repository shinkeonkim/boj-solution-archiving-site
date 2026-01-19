#include <iostream>
#include <string>
using namespace std;
string a;
int ar[330],A,Max,Cnt;
int main()
{
    cin>>a;
    
    for(int x=0; x<a.length(); x++)
    {
        if(a[x]>=97) a[x]-=32;
        ar[a[x]]++;
    }
    for(int x=0; x<320; x++)
    {
        if(ar[x]>Max) 
        {
            Max=ar[x];
            A=x;
        }
    }
    for(int x=0; x<320; x++)
    {
        if(ar[x]==Max) Cnt++;
    }
    if(Cnt>1) cout<<"?";
    else cout<<(char)A;
}