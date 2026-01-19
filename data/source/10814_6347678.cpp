#include <iostream>
#include <algorithm>
using namespace std;
struct person
{
	int age,num;
	char name[104];	
};
int n;
person ar[100005];
int Compare(person a,person b)
{
	if(a.age<b.age) return true;
	if(a.age==b.age)
	{
		if(a.num<b.num) return true;
	}
	return false;
}
int main()
{
	cin>>n;
	for(int x=0; x<n; x++)
	{
		scanf("%d %s",&ar[x].age,ar[x].name);
		ar[x].num=x;
	}
	
	sort(ar,ar+n,Compare);
	
	for(int x=0; x<n; x++)
	{
		printf("%d %s\n",ar[x].age,ar[x].name);
	}
}