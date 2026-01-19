#include <iostream>
#include <string>
using namespace std;
int N,C;
string ar[110];
int main()
{
	cin>>N;
	getline(cin,ar[0]);
	for(int x=0; x<N; x++) getline(cin,ar[x]);
	for(int x=0; x<N; x++)
	{
		C=0;
		for(int y=0; y<ar[x].length(); y++)
		{
			if(C==1&&ar[x][y]!=' ')
			{
				cout<<ar[x][y];
			}
			if(C==0&&ar[x][y]==' ')
			{
				cout<<"god";
				C=1;
			}
		}
		cout<<endl;
	}
}