#include <iostream>
#include <cstdio>
using namespace std;
int N,S,Ball,ans;
int ar[110][5];
int A[110],B[110];
int main()
{
	cin>>N;
	for(int x=0; x<N; x++)
	{
		for(int y=0; y<3; y++) scanf("%1d",&ar[x][y]);
		cin>>A[x]>>B[x];
	}
	/*
	for(int x=0; x<N; x++)
	{
		for(int y=0; y<3; y++) cout<<ar[x][y]<<" ";
		cout<<endl;
	}*/
	
	
	for(int a=1; a<10; a++)
	{
		for(int b=1; b<10; b++)
		{
			for(int c=1; c<10; c++)
			{
				int Cnt=0;
				for(int x=0; x<N; x++)
				{
					S=Ball=0;
					if(ar[x][0]==a) S++;
					else if(ar[x][1]==a) Ball++;
					else if(ar[x][2]==a) Ball++;
					
					if(ar[x][1]==b) S++;
					else if(ar[x][0]==b) Ball++;
					else if(ar[x][2]==b) Ball++;
					
					if(ar[x][2]==c) S++;
					else if(ar[x][0]==c) Ball++;
					else if(ar[x][1]==c) Ball++;
					
					if(A[x]==S&&B[x]==Ball) Cnt++;
				}
				if(Cnt==N&&a!=b&&b!=c&&a!=c)
				{
					ans++;
					//cout<<a<<b<<c<<endl;
				}
			}
		}
	}
	cout<<ans;
}