#include <iostream>
#include <string>
using namespace std;
string ar;
int start,Cnt;
int main()
{
    getline(cin,ar);
    for(int x=0; x<ar.length(); x++)
    {
        if(ar[x]==' ') start++;
        else break;
    }
    for(int x=start; x<ar.length(); x++)
    {
        if(ar[x]==' ') Cnt++;
    }
    if(ar[ar.length()-1]!=' ') Cnt++;
    cout<<Cnt;
}