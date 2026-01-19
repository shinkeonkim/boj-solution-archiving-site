#include <stdio.h>
#include <stdlib.h> 
int main()
{
	int a;
	while(1)
	{
		a=getchar();
		if(a==EOF) break;
		putchar(a);	
	}
}