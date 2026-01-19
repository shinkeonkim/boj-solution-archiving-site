#include <iostream>
#include <string>
using namespace std;
int T,a,b;
string s;
int main()
{
    cin>>T;
    for(int t=0; t<T; t++)
    {
        cin>>a>>b>>s;
        for(auto iter=s.begin(); iter != s.end(); ++iter)
        {
            cout<<(char) ((a*((*iter)-'A')+b)%26 + 'A');
        }
        cout<<endl;
    }
}