#include <iostream>
using namespace std;
int a,b,c,d;
int main()
{
	cin>>a>>b>>c>>d;
	if(b==c&&(a==8||a==9)&&(d==8||d==9)) cout<<"ignore";
	else cout<<"answer";
}