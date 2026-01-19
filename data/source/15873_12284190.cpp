#include <iostream>
#include <string>
using namespace std;
string a;
int main()
{
    cin>>a;
    if(a.size()==4)
    {
        cout<<20;
    }
    else if(a.size()==3)
    {
        if(a[1]=='0')
        {
            cout<<10+a[2]-'0';
        }
        else cout<<10+a[0]-'0';
    }
    else
    {
        cout<<a[0]+a[1]-'0'*2;
    }
}