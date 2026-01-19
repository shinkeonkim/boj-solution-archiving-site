#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int A;
vector <int> V;
int main()
{
    while(1)
    {
        while(!V.empty()) V.pop_back();
        cin>>A;
        if(A==-1) return 0;
        else 
        {
            int S=1;
            V.push_back(1);
            for(int x=2; x*x<=A; x++)
            {
                if(A%x==0)
                {
                    if(x*x==A)
                    {
                        S+=x;
                        V.push_back(x);
                    }
                    else
                    {
                        S+=x+(A/x);
                        V.push_back(x);
                        V.push_back(A/x);
                    }
                }
            }

            if(S==A)
            {
                sort(V.begin(),V.end());
                cout<<A<<" =";
                for(int x=0; x<V.size(); x++)
                {
                    if(x==V.size()-1)
                    {
                        cout<<" "<<V[x]<<"\n";
                    }
                    else
                    {
                        cout<<" "<<V[x]<<" +";
                    }
                }
            }
            else
            {
                cout<<A<<" is NOT perfect.\n";
            }
            
            
        }
    }
}