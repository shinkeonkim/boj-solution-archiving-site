#include <iostream>
using namespace std;
int A,B,C;
int main()
{
    cin>>A>>B>>C;
    if(C%2==1)
    {
        cout<< (A^B);
    }
    else
    {
        cout<<A;
    }
}