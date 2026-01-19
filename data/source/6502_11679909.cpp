#include <iostream>
using namespace std;
int R,A,B,K=1;
int main()
{
	while(1)
	{
		cin>>R;
		if(R==0) return 0;
		else
		{
			cin>>A>>B;
			if(4*R*R>=A*A+B*B)
			{
				cout<<"Pizza "<<K<<" fits on the table.\n";
			}
			else cout<<"Pizza "<<K<<" does not fit on the table.\n";
			K++;
		}
	}
}