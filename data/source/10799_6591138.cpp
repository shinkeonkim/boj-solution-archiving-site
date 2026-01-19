#include<iostream>
#include <string.h>
using namespace std;
char ar[100010];
int Cnta,Cnt;
int main()
{
	scanf("%s",ar);
	for(int x=0; x<strlen(ar); x++)
	{
		if(ar[x]=='(')
		{
			if(ar[x+1]==')')
			{
				Cnt+=Cnta;
				x++;
				//printf("%d ",Cnta);
			}
			else Cnta++;
		}
		else if(ar[x]==')') Cnta--,Cnt++;
	}
	printf("%d",Cnt);
}