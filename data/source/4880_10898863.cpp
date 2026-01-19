#include <iostream>
using namespace std;
int a,b,c;
int main()
{
	while(1)
	{
		cin>>a>>b>>c;
		if(a==0&&b==0&&c==0) return 0;
		else if(a*c==b*b) cout<<"GP "<<c*(b/a)<<endl;
		else if(a+c==2*b) cout<<"AP "<<c+(b-a)<<endl;
	}
}