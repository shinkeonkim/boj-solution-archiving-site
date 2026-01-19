#include <iostream>
#include <string>
using namespace std;
int T;
int a,b;
string str;
char c;
int main()
{
    cin>>str>>T;
    for(int x=0; x<T; x++)
    {
        cin>>a>>b;
        c=str[a];
        str[a]=str[b];
        str[b]=c;
    }
    cout<<str;
}