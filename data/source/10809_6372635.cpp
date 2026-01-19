#include<iostream>
#include<string.h>
using namespace std;
int ar[26];
char ss[110];
int main()
{
	//a=97,z=122, -97 => 0~25
	 scanf("%s",ss);
	 for(int x=0; x<26; x++)ar[x]=-1;
	 for(int x=strlen(ss)-1; x>=0; x--)
	 {
	 	ar[ss[x]-97]=x;
	 }
	 for(int x=0; x<26; x++)
	 {
	 	printf("%d ",ar[x]);
	 }
	
	
}