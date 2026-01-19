#include <bits/stdc++.h>
using namespace std;
string ar;
int a,b,c,d;
int main()
{
    while(getline(cin,ar))
    {   
        a=b=c=d=0;
        for(int x=0; x<ar.length(); x++)
        {
            if('a'<=ar[x]&&ar[x]<='z') a++;
            if('A'<=ar[x]&&ar[x]<='Z') b++;
            if('0'<=ar[x]&&ar[x]<='9') c++;
            if(ar[x] == ' ') d++;
        }
        cout<<a<<" "<<b<<" "<<c<<" "<<d<<"\n";
    }
}