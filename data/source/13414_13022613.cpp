#include <iostream>
#include <map>
#include <string>
#include <algorithm>
using namespace std;

struct st
{
    string a;
    int K;
};

map <string , int> M;
st ar[550000];

int k,N,C;
string A;

bool compare(st X,st Y)
{
    if(X.K<Y.K) return true;
    return false;
}

int main()
{
    cin>>k>>N;

    for(int x=0; x<N; x++)
    {
        cin>>A;
        M[A]=x;
    }

    C=0;
    for(auto iter= M.begin(); iter!=M.end(); ++iter)
    {
        ar[C].a= iter -> first;
        ar[C].K= iter -> second;
        C++;
    }

    sort(ar,ar+C,compare);
    
    for(int x=0; x<k && x<C; x++)
    {
        cout<<ar[x].a<<"\n";
    }
}