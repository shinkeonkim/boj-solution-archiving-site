#include <iostream>
#include <ctime>
#include <cstdlib>
using namespace std;
int main()
{
    int a;
    for(int x=0; x<100000000; x++) a = rand() & 1;
    if(time(0)%2==1)
    {
        cout<<"Korea";
    }
    else 
        cout<<"Yonsei";
}