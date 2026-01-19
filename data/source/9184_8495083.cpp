#include <iostream>
using namespace std;
int ar[50][50][50],A,B,C;
int w(int a, int b,int c)
{
	if(ar[a][b][c]) return ar[a][b][c];
	if(a <= 0 || b <= 0 || c <= 0) return ar[a][b][c] = 1;
	if(a > 20 || b > 20 || c > 20) ar[a][b][c]=w(20, 20, 20);
	if(a < b && b < c) return ar[a][b][c]= w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c);
    else return ar[a][b][c]=w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1);
}
int main()
{
	cin>>A>>B>>C;
	while(!(A==-1&&B==-1&&C==-1))
	{
		cout<<"w("<<A<<", "<<B<<", "<<C<<") = ";
		if(A<=0||B<=0||C<=0) cout<<"1";
		else if(A>20||B>20||C>20) cout<<w(20,20,20);
		else cout<<w(A,B,C);
		cout<<endl;
		cin>>A>>B>>C;
	}
	
	
}

