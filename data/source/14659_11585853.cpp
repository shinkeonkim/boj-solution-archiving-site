#include <iostream>
#include <stack>
using namespace std;
int N,ar[33000],check[3000];
stack <int> Value;
stack <int> array;
long long A;
int main()
{
    cin>>N;
    for(int x=0; x<N; x++) cin>>ar[x];
     
    for(int x=0; x<N; x++)
    {
        if(Value.empty())
        {
            Value.push(ar[x]);
            array.push(x);
        }
        else
        {
            while(!Value.empty()&&ar[x]>=Value.top())
            {
                check[array.top()]=x-array.top()-1;
                array.pop();
                Value.pop();
            }
            Value.push(ar[x]);
            array.push(x);
        }   
    }
     
    while(!array.empty())
    {
        check[array.top()]=N-1-array.top();
        array.pop();
    }
    check[N-1]=0;
    for(int x=0; x<N; x++)
    {
    	if(A<check[x]) A=check[x];
	}
    cout<<A;
}