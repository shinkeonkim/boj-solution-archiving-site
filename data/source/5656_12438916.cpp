#include <bits/stdc++.h>
using namespace std;
int A,B,Cnt=1;
string a;
int main()
{
    while(1)
    {
        cin>>A>>a>>B;
        if(a=="E") return 0;
        cout<<"Case "<<Cnt<<": ";
        Cnt++;
        if(a==">")
        {
            if(A>B) cout<<"true";
            else cout<<"false";
        }
        if(a==">=")
        {
            if(A>=B) cout<<"true";
            else cout<<"false";
        }
        if(a=="<")
        {
            if(A<B) cout<<"true";
            else cout<<"false";
        }
        if(a=="<=")
        {
            if(A<=B) cout<<"true";
            else cout<<"false";
        }
        if(a=="==")
        {
            if(A==B) cout<<"true";
            else cout<<"false";
        }
        if(a=="!=")
        {
            if(A!=B) cout<<"true";
            else cout<<"false";
        }
        cout<<endl;
    }
}