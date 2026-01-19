#include <iostream>
#include <algorithm>
using namespace std;
int a[10];
int ar[11000];
int im[10],Cnt,K;
int main()
{
	for(int x=0; x<4; x++) cin>>a[x];
	
	im[0]=a[0]*1000+a[1]*100+a[2]*10+a[3];
	im[1]=a[1]*1000+a[2]*100+a[3]*10+a[0];
	im[2]=a[2]*1000+a[3]*100+a[0]*10+a[1];
	im[3]=a[3]*1000+a[0]*100+a[1]*10+a[2];
	
	sort(im,im+4);
	K=im[0];
	
	for(int A=1; A<=9; A++)
	{
		for(int B=1; B<=9; B++)
		{
			for(int C=1; C<=9; C++)
			{
				for(int D=1; D<=9; D++)
				{
					im[0]=A*1000+B*100+C*10+D;
					im[1]=B*1000+C*100+D*10+A;
					im[2]=C*1000+D*100+A*10+B;
					im[3]=D*1000+A*100+B*10+C;
					
					sort(im,im+4);
					ar[Cnt++]=im[0];		
				}
			}
		}
	}
	sort(ar,ar+Cnt);
	int Z=1;
	if(ar[0]==K)
	{
		cout<<1;
		return 0;
	}
	
	for(int x=1; x<Cnt; x++)
	{
		if(ar[x]!=ar[x-1]) Z++;
		
		if(ar[x]==K)
		{
			cout<<Z;
			return 0;
		}
	}
	
}
