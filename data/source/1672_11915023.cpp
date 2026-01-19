#include <iostream>
#include <map>
#include <string>
#include <vector>
using namespace std;
map <char ,int> M;
int N;
string a;
vector <char> V;
char ar[4][4]={'A','C','A','G','C','G','T','A','A','T','C','G','G','A','G','T'};
int main()
{
	cin>>N>>a;
	for(int x=0; x<N; x++) V.push_back(a[x]);
	M['A']=0;
	M['G']=1;
	M['C']=2;
	M['T']=3;
	for(int x=1; x<N; x++)
	{
		char X=V.back();
		V.pop_back();
		char Y=V.back();
		V.pop_back();
		V.push_back(ar[M[Y]][M[X]]);
	}
	cout<<V[0];
} 