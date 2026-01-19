#include <iostream>
#define Mx 98765432
using namespace std;
int T,A;
int a,b,c,d,Min;
int main()
{
    //그냥 브루트 포스
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    cin>>T;
    for(int t=0; t<T; t++)
    {
        cin>>A;
        Min=Mx;
        for(int x=0; x<=A/25; x++)
        {
            for(int y=0; y<=A/10; y++)
            {
                for(int z=0; z<=A/5; z++)
                {
                    int q=A-(25*x+y*10+z*5);
                    if(q>-1&&x+y+z+q<Min)
                    {
                        Min=x+y+z+q;
                        a=x;
                        b=y;
                        c=z;
                        d=q;
                    }
                }
            }
        }
        cout<<a<<" "<<b<<" "<<c<<" "<<d<<endl;
    }
}