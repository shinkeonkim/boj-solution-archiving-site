#include <iostream>
using namespace std;
int N;
int main()
{
    cin>>N;
    N+=56;
    cout<<(char)(N%12+'A')<<N%10;
}