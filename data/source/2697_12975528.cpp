#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
using namespace std;
int N;
string ar[1100];
vector <char> V;
int main()
{
    cin>>N;
    for(int x=0; x<N; x++) cin>>ar[x];

    for(int x=0; x<N; x++)
    {
        V.clear();
        for(int y=0; y<ar[x].size(); y++) V.push_back(ar[x][y]); 
        if(next_permutation(V.begin(),V.end()))
        {
            for(int y=0; y<V.size(); y++) cout<<V[y]; 
        }
        else cout<<"BIGGEST";
        cout<<"\n";
    }
}