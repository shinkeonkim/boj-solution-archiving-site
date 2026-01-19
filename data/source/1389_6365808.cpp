#include <stdio.h>
int ar[105][105],N,M,flag,Min=99999;
int main()
{
	scanf("%d %d",&N,&M);
	for(int q=0; q<N; q++)
		for(int p=0; p<N; p++)
		{
			if(p==q)ar[q][p]=0;
			else ar[q][p]=9999999;
		 } 
	for(int q=0; q<M; q++)
	{
		int a,b;
		scanf("%d %d",&a,&b);
		ar[a-1][b-1]=1;
		ar[b-1][a-1]=1;
	}
	for(int k=0; k<N; k++)
		for(int q=0; q<N; q++)
			for(int p=0;p<N; p++)
			{
				if(ar[q][p]>ar[q][k]+ar[k][p])
				ar[q][p]=ar[q][k]+ar[k][p];
			}
			
	for(int q=N-1; q>=0; q--)
	{
		int Sum=0;
		for(int p=0;p<N; p++)
		{
			Sum+=ar[q][p];
		}
		if(Sum<=Min)
		{
			Min=Sum;
			flag=q;
		}
	}
	printf("%d",flag+1);
			
}