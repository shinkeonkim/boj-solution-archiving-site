#include <iostream>
#include <algorithm>
using namespace std;
int N,size,heap[100200];
int main()
{
	scanf("%d",&N);
	for(int x=0; x<N; x++)
	{
		int a;
		scanf("%d",&a);
		if(a>0)
		{
			heap[size++]=a;
			push_heap(heap,heap+size);
		}
		else if(a==0)
		{
			
			if(size<1) printf("0\n");
			else
			{
				printf("%d\n",heap[0]);
				pop_heap(heap,heap+size);
				size--;
			}
		}
	}
}