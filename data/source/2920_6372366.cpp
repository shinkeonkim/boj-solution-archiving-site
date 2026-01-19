#include <iostream>
using namespace std;
int ar[9],aCnt,bCnt;
int main()
{
	
	for(int x=1; x<=8; x++)scanf("%d",&ar[x]);
	for(int x=1; x<=8; x++)
	{
		if(x==ar[x])aCnt++;
		if(9-x==ar[x]) bCnt++;
	}
	if(aCnt==8)printf("ascending");
	else if(bCnt==8) printf("descending");
	else printf("mixed");
		
} 