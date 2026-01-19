#include <iostream>
#include <algorithm>
using namespace std;
int n,q;
int Memo[20];
char ar[20],ar2[20];

int Backtrack(int w,int e)
{
	if(w==n)
	{
		
		int aCnt=0,bCnt=0;
		for(int x=0; x<n; x++)
		{
			if(ar2[x]=='a'||ar2[x]=='e'||ar2[x]=='i'||ar2[x]=='o'||ar2[x]=='u') aCnt++;
			else bCnt++;
		}
		
		
		if(aCnt>0&&bCnt>1)
		{
		for(int x=0; x<n; x++) printf("%c",ar2[x]);
		printf("\n");	
		}
		
	}
	else
	{
		for(int r=e+1; r<q; r++)
		{
			if(Memo[r]==0)
			{
				ar2[w]=ar[r];
				Memo[r]=1;
				Backtrack(w+1,r);
				Memo[r]=0;
			}
		}
	}
}
int main()
{
	scanf("%d %d\n",&n,&q);
	for(int x=0; x<q; x++) cin>>ar[x];
	sort(ar,ar+q);
	for(int x=0; x<q; x++)
	{
		ar2[0]=ar[x];
		Memo[x]=1;
		Backtrack(1,x);
		Memo[x]=0;
	}
}