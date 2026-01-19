#include <iostream>
using namespace std;
int T,A;
int main()
{
    cin>>T;
    for(int x=0; x<T; x++)
    {
        cin>>A;
        if(A==1||A==2)
        {
            for(int x=0; x<A; x++)
            {
                for(int y=0; y<A; y++)
                {
                    cout<<"#";
                }
                cout<<endl;
            }
            cout<<endl;
            continue;
        }

        for(int y=0; y<A; y++)
        {
            for(int x=0; x<A; x++)
            {
                if(x==0||y==0||x==A-1||y==A-1) cout<<"#";
                else cout<<"J";
            }
            cout<<endl;
        }
        cout<<endl;
    }
}