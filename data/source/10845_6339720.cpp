#include <iostream>
#include <queue>
#include <stdio.h>
using namespace std;
int n;
char ar[10];
int main()
{
	queue <int> qu;
	scanf("%d",&n);
	for(int x=0; x<n; x++)
	{
		for(int y=0; y<10; y++)ar[y]='0';
		scanf("%s",ar);
		if(ar[0]=='p')
		{
			if(ar[1]=='o')//pop
			{
				if(qu.empty()) printf("-1\n");
				else
				{
					printf("%d\n",qu.front());
					qu.pop();
				}
			}
			else //push
			{
				int a;
				scanf("%d\n",&a);
				qu.push(a);
			}
		}
		else if(ar[0]=='f') //front
		{
			if(qu.empty()) printf("-1\n");
				else
				{
					printf("%d\n",qu.front());
				}
		}
		else if(ar[0]=='b') //back
		{
			if(qu.empty()) printf("-1\n");
				else
				{
					printf("%d\n",qu.back());
				}
		}
		else if(ar[0]=='s') //size
		{
			printf("%d\n",qu.size());
		}
		else if(ar[0]=='e')
		{
			if(qu.empty()) printf("1\n");
			else printf("0\n");
		}
	}
}