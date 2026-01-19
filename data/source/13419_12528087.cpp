#include <bits/stdc++.h>
using namespace std;
int N;
string a;
int main()
{
    cin>>N;
    for(int t=0; t<N; t++)
    {
        cin>>a;
        if(a.length()%2==0)
        {
            for(int x=0; x<a.length(); x+=2)
            {
                cout<<a[x];
            }
            cout<<endl;
            for(int x=1; x<a.length(); x+=2)
            {
                cout<<a[x];
            }
            cout<<endl;
        }
        else
        {
            for(int x=0; x<a.length(); x+=2)
            {
                cout<<a[x];
            }
            for(int x=1; x<a.length(); x+=2)
            {
                cout<<a[x];
            }
            cout<<endl;


            for(int x=1; x<a.length(); x+=2)
            {
                cout<<a[x];
            }
            for(int x=0; x<a.length(); x+=2)
            {
                cout<<a[x];
            }
            cout<<endl;
        }
        
    }
    
}