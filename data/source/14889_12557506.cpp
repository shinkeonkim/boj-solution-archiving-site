#include <bits/stdc++.h>
#define Mx 987654321
using namespace std;
int N,Min=Mx;
int ar[22];
int D[22][22];
vector <int> V1;
vector <int> V2;
int main()
{
    cin>>N;
    for(int y=0; y<N; y++)
    {
        for(int x=0; x<N; x++) cin>>D[y][x];
    }
    for(int x=N/2; x<N; x++) ar[x]=1;

    do
    {
        V1.clear();
        V2.clear();
        for(int x=0; x<N; x++)
        {
            if(ar[x]==1) V2.push_back(x);
            else V1.push_back(x);
        }
        int S1=0;
        int S2=0;
        for(auto iter=V1.begin(); iter != V1.end(); iter++)
        {
            for (auto iter2 = V1.begin(); iter2 != V1.end(); iter2++)
            {
                S1+=D[*iter][*iter2];
            }
        }

        for(auto iter=V2.begin(); iter != V2.end(); iter++)
        {
            for (auto iter2 = V2.begin(); iter2 != V2.end(); iter2++)
            {
                S2+=D[*iter][*iter2];
            }
        }
        if(abs(S1-S2)<Min) Min=abs(S1-S2);
    }
    while(next_permutation(ar,ar+N));
    cout<<Min;
}