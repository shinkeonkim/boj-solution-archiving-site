#include <iostream>
#include <string> 
using namespace std;
string ar;
int check[50]; 
int main()
{   //-97= > 0~25
	cin>>ar;
	for(int x=0; x<ar.length(); x++)
	{
		check[ar[x]-97]++;
	}
	for(int x=0; x<26; x++) cout<<check[x]<<" ";
}