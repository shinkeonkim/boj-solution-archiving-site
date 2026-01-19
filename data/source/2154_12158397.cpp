#include <iostream>
#include <string>
using namespace std;
int N;
string a;
string b;
void f(int x)
{
    if(x>0)
    {
        f(x/10);
        a.push_back(x%10+'0');
    }
}
void f2(int y)
{
    if(y>0)
    {
        f2(y/10);
        b.push_back((y%10)+'0');
    }
}
int main()
{
    cin>>N;
    for(int x=1; x<=N; x++)
    {
        f(x);
    }
    f2(N);
    for(int x=0; x+b.length()-1<a.length(); x++)
    {
        int C=0;
        for(int y=0; y<b.length(); y++)
        {
            if(b[y]!=a[x+y]) C=1;
        }
        if(C==0)
        {
            cout<<x+1;
            return 0;
        }
    }
}