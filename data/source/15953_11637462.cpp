#include <iostream>
using namespace std;
int T,A,B;
int f(int X)
{
	if(X==1) return 500;
	else if(2<=X&&X<=3) return 300;
	else if(4<=X&&X<=6) return 200;
	else if(7<=X&&X<=10) return 50;
	else if(11<=X&&X<=15) return 30;
	else if(16<=X&&X<=21) return 10;
	else return 0;
}
int g(int X)
{
	if(X==1) return 512;
	else if(2<=X&&X<=3) return 256;
	else if(4<=X&&X<=7) return 128;
	else if(8<=X&&X<=15) return 64;
	else if(16<=X&&X<=31) return 32;
	else return 0;
}
int main()
{
	cin>>T;
	for(int x=0; x<T; x++)
	{
		cin>>A>>B;
		if(f(A)+g(B)!=0) cout<<(f(A)+g(B))<<"0000\n";
		else cout<<0<<endl;
	}
}