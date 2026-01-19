#include <iostream>
#include <string>
using namespace std;
int N,Cnt,Cnt1,Cnt2,Cnt3,Cnt4;
string a;
string ar[110];
int check[110][110];
//65 90
int main()
{
    cin>>N;
    for(int x=0; x<N; x++)
    {
        cin>>ar[x];
    }
    for(int x=0; x<N; x++)
    {
        for(int y=0; y<ar[x].length(); y++)
        {
            check[x][(int)ar[x][y]]++;
        }
    }
    for(int x=1; x<N; x++)
    {
        int Cnt1=Cnt2=Cnt3=Cnt4=0;
        for(int y=65; y<=90; y++)
        {
            if(check[0][y]>check[x][y])
            {
                Cnt1+=check[0][y]-check[x][y];
            }
            else if(check[0][y]<check[x][y])
            {
                Cnt2+=check[x][y]-check[0][y];
            }
        }
        if(Cnt1>0&&Cnt2>0)
        {
            Cnt1--;
            Cnt2--;
        }else if(Cnt1>0)
        {
            Cnt1--;
        }
        else if(Cnt2>0)
        {
            Cnt2--;
        }
        if(Cnt1+Cnt2==0)
        {
            Cnt++;
        }
        //cout<<x<<" "<<Sum<<endl;  
    }
    cout<<Cnt;
}