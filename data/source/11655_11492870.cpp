#include <iostream>
#include <string>
using namespace std;
string a;
int K;
int main()
{
	getline(cin,a);
	for(int x=0; x<a.length(); x++)
	{
		if('A'<=a[x]&&a[x]<='Z')
		{
			K=a[x]-'A';
			K+=13;
			if(K>25) K-=26;
			cout<<(char)(K+'A');	
		}
		else if('a'<=a[x]&&a[x]<='z')
		{
			K=a[x]-'a';
			K+=13;
			if(K>25) K-=26;
			cout<<(char)(K+'a');
		}
		else cout<<a[x];
	}
}