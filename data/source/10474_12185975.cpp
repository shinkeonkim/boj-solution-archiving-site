#include <iostream>
using namespace std;
int a,b;
int main()
{
    while(1)
    {
        cin>>a>>b;
        if(a==0&&b==0) return 0;
        cout<<a/b<<" ";
        if(a%b==0) cout<<"0 / "<<b;
        else
        {
            a=a%b;
            cout<<a<<" / "<<b;
        }
        cout<<endl;
        
    }
}