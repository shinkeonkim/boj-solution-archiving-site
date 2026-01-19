#include <iostream>
using namespace std;

struct st{
    char L_node,R_node;
};

int N;
st Tree[33];
char a,b,c;

void f1(char x);
void f2(char x);
void f3(char x);

int main()
{
    cin>>N;
    for(int x=0; x<N; x++)
    {
        cin>>a>>b>>c;
        Tree[a-'A'].L_node=b;
        Tree[a-'A'].R_node=c;
    }
    f1('A');
    cout<<endl;
    f2('A');
    cout<<endl;
    f3('A');
}

void f1(char x)
{
    cout<<x;
    if(Tree[x-'A'].L_node!='.') f1(Tree[x-'A'].L_node);
    if(Tree[x-'A'].R_node!='.') f1(Tree[x-'A'].R_node);
}
void f2(char x)
{
    if(Tree[x-'A'].L_node!='.') f2(Tree[x-'A'].L_node);
    cout<<x;
    if(Tree[x-'A'].R_node!='.') f2(Tree[x-'A'].R_node);
}
void f3(char x)
{
    if(Tree[x-'A'].L_node!='.') f3(Tree[x-'A'].L_node);
    if(Tree[x-'A'].R_node!='.') f3(Tree[x-'A'].R_node);
    cout<<x;
}