#include <iostream>
#include <string.h>
using namespace std;
string a,b;
char tmp;
int main()
{
	cin>>a>>b;
	
	tmp=a[0];a[0]=a[2];a[2]=tmp;
	tmp=b[0];b[0]=b[2];b[2]=tmp;
	
	if(a.compare(b)>0)cout<<a;
	else cout<<b; 
	
}