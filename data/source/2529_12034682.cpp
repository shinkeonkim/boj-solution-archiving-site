#include <iostream>
#include <string>
using namespace std;
unsigned long long int Min=9999999999,Max=0;
unsigned long long int check[21],numcheck[21],Mincheck[21],Maxcheck[21];
int N;
string a;
void g()
{
	unsigned long long int K=0;
	for(int x=0; x<=N; x++)
	{
		//cout<<check[x];
		K*=10;
		K+=check[x];
	}
	//cout<<endl;
	
	if(K>Max)
	{
		 Max=K;
		 for(int x=0; x<=N; x++)Maxcheck[x]=check[x];
	}
	if(K<Min)
	{
		 Min=K;
		 for(int x=0; x<=N; x++)Mincheck[x]=check[x];
	}
}
int f(int n)
{
	if(n==N)
	{
		if(a[(n-1)*2]=='<')
		{
			for(int x=check[n-1]+1; x<=9; x++)
			{
				if(numcheck[x]!=1)
				{
					check[n]=x;
					g();	
				}
				
			}
		}
		else 
		{
			for(int x=0; x<check[n-1]; x++)
			{
				if(numcheck[x]!=1)
				{
					check[n]=x;
					g();	
				}
			}
		}
	}
	else
	{
		if(a[(n-1)*2]=='<')
		{
			for(int x=check[n-1]+1; x<=9; x++)
			{
				if(numcheck[x]!=1)
				{
					check[n]=x;
					numcheck[x]=1;
					f(n+1);	
					numcheck[x]=0;
				}
				
			}
		}
		else 
		{
			for(int x=0; x<check[n-1]; x++)
			{
				if(numcheck[x]!=1)
				{
					numcheck[x]=1;				
					check[n]=x;
					f(n+1);	
					numcheck[x]=0;
				}
			}
		}
	}
}
int main()
{
	cin>>N;getline(cin,a);
	getline(cin,a);
	
	for(int x=0; x<=9; x++)
	{
		check[0]=x;
		numcheck[x]=1;
		f(1);
		numcheck[x]=0;
	}
	for(int x=0; x<=N; x++)cout<<Maxcheck[x];
	cout<<endl;
	for(int x=0; x<=N; x++)cout<<Mincheck[x];
	cout<<endl;
}
