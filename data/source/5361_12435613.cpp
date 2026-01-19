#include <iostream>
#include <cstdio>
using namespace std;
int N;
int ar[8];
int A[]={350,230,190,125,180};
int B[]={34,90,55,30,90};
int Sa,Sb;
int main()
{
    cin>>N;
    for(int t=0; t<N; t++)
    {
        for(int x=0; x<5; x++) cin>>ar[x];
        Sa=Sb=0;
        for(int x=0; x<5; x++)
        {
            Sa+=ar[x]*A[x];
            Sb+=ar[x]*B[x];
        }
        printf("$%d.%02d\n",Sa+Sb/100,Sb%100);
    }
}