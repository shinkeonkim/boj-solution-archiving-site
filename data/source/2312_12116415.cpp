#include <iostream>
#include <vector>
using namespace std;
int T,A;
int M[110000];
vector <int> V;
int main()
{
    for(int x=2; x<=100000; x++)
    {
        if(M[x]!=1)
        {
            V.push_back(x);
            for(int y=x+x; y<=100000; y+=x)
            {
                M[y]=1;
            }
        }
    }
    cin>>T;
    for(int x=0; x<T; x++)
    {
        cin>>A;
        for(int y=0; y<V.size(); y++)
        {
            int Cnt=0;
            while(A%V[y]==0&&A!=0)
            {
                Cnt++;
                A/=V[y];
            }
            if(Cnt>0)cout<<V[y]<<" "<<Cnt<<endl;
        }
    }

}