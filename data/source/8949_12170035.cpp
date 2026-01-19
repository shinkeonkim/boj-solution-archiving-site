#include <iostream>
#include <stack>
using namespace std;
int a,b;
stack <int> S;
int main()
{
    cin>>a>>b;
    while(a>0||b>0)
    {
        S.push((a%10)+(b%10));
        a/=10;
        b/=10;
    }
    while(!S.empty())
    {
        cout<<S.top();
        S.pop();
    }

}