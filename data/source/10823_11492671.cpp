#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
char ar[11000];
int S,A;
int main()
{
	while(scanf("%s",ar)!=EOF)
	{
		for(int x=0; x<strlen(ar); x++)
		{
			if(ar[x]!=',')
			{
				A*=10;
				A+=ar[x]-'0';
			}
			else if(ar[x]==',') 
			{
				S+=A;
				A=0;	
			}
		}	
	}
	S+=A;
	cout<<S;
}