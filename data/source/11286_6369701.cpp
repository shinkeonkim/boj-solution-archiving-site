#include <iostream>
#include <algorithm>
using namespace std;
int N,size,heap[100200];
bool compare(int a, int b)
{
	int A=a;
	int B=b;
	if(A<0) A=-A;
	if(B<0) B=-B; 
	
	if(A>B) return true;
	else if((a>0&&b<0)&&A==B)
	{
		return true;	
	} 
	else return false;
}
int main()
{
	scanf("%d",&N);
	for(int x=0; x<N; x++)
	{
		int a;
		scanf("%d",&a);
		if(a!=0)
		{
			heap[size++]=a;
			push_heap(heap,heap+size,compare);
		}
		else if(a==0)
		{
			
			if(size<1) printf("0\n");
			else
			{
				printf("%d\n",heap[0]);
				pop_heap(heap,heap+size,compare);
				size--;
			}
		}
	}
}