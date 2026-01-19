#include <iostream>
using namespace std;
int a=1,b=1;
int main()
{
	while(1)
	{
		cin>>a>>b;
		if(a==0&&b==0) return 0;
		else cout<<a+b<<endl;
	}
}