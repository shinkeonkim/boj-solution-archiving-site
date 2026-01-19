#include <iostream>
#include <vector>
#include <string>
using namespace std;
int T;
string a,k;
vector <string> V;
int main()
{
    cin>>T;
    getline(cin,a);
    for(int t=1; t<=T; t++)
    {
        while(!V.empty() )V.pop_back();
        getline(cin,a);
        k="";
        for(int x=0; x<a.length(); x++)
        {
            if(a[x]!=' ')
            {
                k.push_back(a[x]);
            }
            else if(a[x]==' ')
            {
                V.push_back(k);
                k="";
            }
            if(x==a.length()-1)
            {
                V.push_back(k);
            }
        }

        cout<<"Case #"<<t<<": ";
        for(int x=V.size()-1; x>-1; x--)
        {
            cout<<V[x]<<" ";
        }
    }
}