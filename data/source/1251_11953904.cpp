#include <iostream>
#include <algorithm>
#include <string>
using namespace std; 
string a,X,Y,Z;
string ar[3300];
int Cnt,i;
int main()
{
	cin>>a;
	for(int x=0; x<a.length(); x++)
	{
		for(int y=x+1; y<a.length(); y++)
		{
			X=Y=Z="";
			for(i=0; i<=x&&i<a.length(); i++) X.push_back(a[i]);
			for(i=x+1; i<=y&&i<a.length(); i++) Y.push_back(a[i]);
			for(i=y+1; i<a.length(); i++) Z.push_back(a[i]);
			if(X.length()!=0&&Y.length()!=0&&Z.length()!=0)
			{
				for(i=X.length()-1; i>-1; i--) ar[Cnt].push_back(X[i]);
				for(i=Y.length()-1; i>-1; i--) ar[Cnt].push_back(Y[i]);
				for(i=Z.length()-1; i>-1; i--) ar[Cnt].push_back(Z[i]);
				Cnt++;
			}
		}
	}
	sort(ar,ar+Cnt);
	cout<<ar[0];
}
