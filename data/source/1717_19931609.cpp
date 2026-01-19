#include <iostream>
using namespace std;
int N,M,a,b,c;


int u[1100000];
int find(int k) {
    if(u[u[k]] == u[k]) return u[k];
    else return u[k]=find(u[k]);
}

void uni(int A, int B) {
    if(A < B) u[B] = A;
    else u[A] = B; 
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    cin>>N>>M;
    for(int x=1; x<=N; x++) u[x]=x;
    for(int x=0; x<M; x++)
    {
        cin>>a>>b>>c;

        if(a == 0)
        {
            int A=find(b);
            int B=find(c);
            uni(A,B);
        }
        else
        {
            if(find(b) != find(c))
            {
                cout<<"NO\n";
            }
            else cout<<"YES\n";
        }
        
    }
}