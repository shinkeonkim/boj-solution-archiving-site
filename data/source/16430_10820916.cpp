#include <iostream>
using namespace std;
int a,b;
int gcd(int x,int y)
{
    return y>0?gcd(y,x%y):x;
}
int main()
{
    cin>>a>>b;
    a=b-a;
    cout<<a/gcd(a,b)<<" "<<b/gcd(a,b);
}