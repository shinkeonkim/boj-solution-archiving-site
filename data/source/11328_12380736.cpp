#include <bits/stdc++.h>
using namespace std;
int N;
string a,b;
vector <char> V1,V2;
int main()
{
    cin>>N;
    for(int x=0; x<N; x++)
    {
        cin>>a>>b;
        for(int x=0; x<a.length(); x++) V1.push_back(a[x]);
        for(int x=0; x<b.length(); x++) V2.push_back(b[x]);

        sort(V1.begin(),V1.end());
        sort(V2.begin(),V2.end());
        int check=1;
        if(V1.size()==V2.size())
        {
            for(int x=0; x<V1.size(); x++)
            {
                if(V1[x]!=V2[x]) check=0;
            }
        }
        else
        {
            check=0;
        }
        if(check==1) cout<<"Possible\n";
        else cout<<"Impossible\n";
        while(!V1.empty())V1.pop_back();
        while(!V2.empty())V2.pop_back();
    }
}