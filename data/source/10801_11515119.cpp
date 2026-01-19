#include <iostream>
using namespace std;
int a[11][2],A,B;
int main()
{
	for(int y=0; y<2; y++)
		for(int x=0; x<10; x++) cin>>a[x][y];
	for(int x=0; x<10; x++)
	{
		if(a[x][0]>a[x][1]) A++;
		else if(a[x][0]<a[x][1]) B++;
	}
	if(A>B) cout<<"A";
	else if(A<B) cout<<"B";
	else cout<<"D";
}