#include <iostream>
using namespace std;
int ar[4400][4400];
int N;

void f(int sy,int sx,int ey, int ex, int n)
{
    //cout<<sy<<" "<<sx<<" "<<ey<<" "<<ex<<" "<<n<<endl;
    if(n==3)
    {
        for(int Y=sy; Y<=ey; Y++)
        {
            for(int X=sx; X<=ex; X++)
            {
                if(Y==sy+1&&X==sx+1);
                else ar[Y][X]=1;
            }
        }
    }
    else
    {
        for(int Y=sy; Y<ey; Y+=n/3)
        {
            for(int X=sx; X<ex; X+=n/3)
            {
                if(Y==sy+n/3 && X==sx+n/3);
                else
                {
                    f(Y,X,Y+n/3-1,X+n/3-1,n/3);
                }
            }
        }
    }
    
}

int main()
{
    cin>>N;
    if(N==1)
    {
        cout<<"*";
        return 0;
    }
    f(0,0,N-1,N-1,N);
    for(int y=0; y<N; y++)
    {
        for(int x=0; x<N; x++)
        {
            if(ar[y][x]==1) cout<<"*";
            else cout<<" ";
        }cout<<endl;
    }
}