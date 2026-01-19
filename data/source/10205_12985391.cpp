#include <iostream>
#include <string>
using namespace std;
int T,N;
string a;
int main()
{
    cin>>T;
    for(int t=0; t<T; t++)
    {
        cin>>N>>a;
        for(auto iter=a.begin(); iter!=a.end(); ++iter)
        {
            if(*iter == 'c') N++;
            else if(*iter == 'b') N--;
        }
        cout<<"Data Set "<<t+1<<":\n";
        cout<<N<<"\n\n";
    }
}