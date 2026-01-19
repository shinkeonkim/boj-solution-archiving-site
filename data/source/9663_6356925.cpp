#include <iostream>
using namespace std;
int n,check1[20],check2[100],check3[100],Cnt;//1 가로 2 대각선+30 수치 
int Backtrack(int q)
{
	if(q==n+1)
	{
		Cnt++;
		return 0;
	}
	else
	{
		for(int x=1; x<=n; x++)
		{
			if(check1[x]==0&&check2[x+q]==0&&check3[x-q+30]==0)
			{
				check1[x]=1;
				check2[x+q]=1;
				check3[x-q+30]=1;
				Backtrack(q+1);
				check1[x]=0;
				check2[x+q]=0;
				check3[x-q+30]=0;
			}
		}
	}
}
int main()
{
	scanf("%d",&n);
	if(n==1) Cnt=1;
	else
	{
		for(int x=1; x<=n; x++)
	{
		check1[x]=1;
		check2[x+1]=1;
		check3[x-1+30]=1;
		Backtrack(2);
		check1[x]=0;
		check2[x+1]=0;
		check3[x-1+30]=0;
	} 	
	}
	printf("%d",Cnt);
}