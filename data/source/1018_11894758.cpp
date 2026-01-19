#include <iostream>
using namespace std;
int N,M,Cnt1,Cnt2,Min=987654321;
char ar[55][55];
int main()
{
	cin>>N>>M;
	for(int y=0; y<N; y++)
	{
		for(int x=0; x<M; x++) cin>>ar[y][x];
	}
	for(int Y=0; Y<N-7; Y++)
	{
		for(int X=0; X<M-7; X++)
		{
			Cnt1=Cnt2=0;
			for(int y=0; y<8; y++)
			{
				for(int x=0; x<8; x++)
				{
					if(ar[Y+y][X+x]=='W')
					{
						if(((X+x)%2==1&&(Y+y)%2==0)||((X+x)%2==0&&(Y+y)%2==1)) Cnt1++;
						if((X+x)%2==(Y+y)%2) Cnt2++;
					}
					if(ar[Y+y][X+x]=='B')
					{
						if(((X+x)%2==1&&(Y+y)%2==0)||((X+x)%2==0&&(Y+y)%2==1)) Cnt2++;
						if((X+x)%2==(Y+y)%2) Cnt1++;
					}
							
				}
			}
			if(Min>Cnt1) Min=Cnt1;
			if(Min>Cnt2) Min=Cnt2;
			
		}
	}
	cout<<Min;
}