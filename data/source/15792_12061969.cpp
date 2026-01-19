#include <iostream>
#define MM 1100
using namespace std;
int A,B;
int main()
{
    cin>>A>>B;
    cout<<(int)(A/B)<<".";
    A=A%B;
    for(int x=0; x<MM; x++)
    {
        A*=10;
        cout<<(int)(A/B);
        A=A%B;
    }
}