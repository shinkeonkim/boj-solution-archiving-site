#include <iostream>
#include <string>
using namespace std;
int N;
string a[33];
int main()
{
	cin>>N;
	for(int x=0; x<N; x++) cin>>a[x];
	
	for(int x=0; x<N; x++)
	{
		if(a[x].length()>1&&a[x][a[x].length()-2]=='n' && a[x][a[x].length()-1]=='e')
		{
			for(int y=0; y<a[x].length()-2; y++) cout<<a[x][y];
			cout<<"anes";
		}
		else
		{
			switch(a[x][a[x].length()-1])
			{
				case 'a':
					a[x].push_back('s');
					break;
				case 'i':
					a[x].push_back('o');
					a[x].push_back('s');
					break;
				case 'y':
					a[x].erase(a[x].end()-1,a[x].end());
					a[x].push_back('i');
					a[x].push_back('o');
					a[x].push_back('s');
					break;
				case 'l':
					a[x].push_back('e');
					a[x].push_back('s');
					break;
				case 'n':
					a[x].erase(a[x].end()-1,a[x].end());
					a[x].push_back('a');
					a[x].push_back('n');
					a[x].push_back('e');
					a[x].push_back('s');
					break;
				case 'o':
					a[x].push_back('s');
					break;
				case 'r':
					a[x].push_back('e');
					a[x].push_back('s');
					break;
				case 't':
					a[x].push_back('a');
					a[x].push_back('s');
					break;
				case 'u':
					a[x].push_back('s');
					break;
				case 'v':
					a[x].push_back('e');
					a[x].push_back('s');
					break;
				case 'w':
					a[x].push_back('a');
					a[x].push_back('s');
					break;
				default:
					a[x].push_back('u');
					a[x].push_back('s');
			}	
			cout<<a[x];
		}
		cout<<endl;
	}
}