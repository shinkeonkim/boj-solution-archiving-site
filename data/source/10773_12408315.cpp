#include <iostream>
#include <stack>
using namespace std;
stack <unsigned long long> stk;
unsigned long long N,A,S;
int main()
{
    cin>>N;
    for(int x=0; x<N; x++)
    {
        cin>>A;
        if(A==0) stk.pop();
        else stk.push(A);
    }
    while(!stk.empty()) 
    {
        S+=stk.top();
        stk.pop();
    }
    cout<<S;
}