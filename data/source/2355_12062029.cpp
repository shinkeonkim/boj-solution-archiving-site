#include <iostream>
using namespace std;
long long A,B;
int main()
{
    cin>>A>>B;
    if(A>=0&&B>=0)
    {
        if(A<B)
        {
            long long K;
            K=A;
            A=B;
            B=K;
        }
        cout<<((A*(A+1))/2)-((B*(B-1))/2);
    
    }
    else if(A>=0&&B<0)
    {
        B=-B;
        cout<<(A*(A+1))/2-(B*(B+1))/2;
    }
    else if(A<0&&B>=0)
    {
        A=-A;
        cout<<-(A*(A+1))/2+(B*(B+1))/2;
    }
    else if(A<0&&B<0)
    {
        A=-A;
        B=-B;
        if(B>A)
        {
            long long T;
            T=A;
            A=B;
            B=T;
        }
        cout<<-((A*(A+1))/2)+((B*(B-1))/2);
    }

}