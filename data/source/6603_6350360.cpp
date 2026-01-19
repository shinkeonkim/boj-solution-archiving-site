#include <iostream>
using namespace std;
int ar[15],Memo[15],Memo2[15],z=1;
int Back(int x,int w)
{
	if(x==6)
	{
		for(int y=0; y<6; y++) printf("%d ",Memo2[y]);
		printf("\n");
		return 0;
	}
	else
	{
		for(int r=w; r<z; r++)
		{
			if(Memo[r]==0) 
			{
				Memo2[x]=ar[r];
				Memo[r]=1;
				Back(x+1,r);
				Memo[r]=0;	
			}			
		}

	}
}
int main()
{
	z=1;
	while(z!=0)
	{
		for(int x=0; x<z; x++) ar[x]=0;
		scanf("%d",&z);
		if(z==0) return 0;
		else
		{
			for(int x=0; x<z; x++)
			{
				scanf("%d",&ar[x]);		
			}
			
			for(int q=0; q<z; q++)
			{
				Memo2[0]=ar[q];
				Memo[q]=1;
				Back(1,q);
				Memo[q]=0;		
			}

		}
		printf("\n");
	}
}