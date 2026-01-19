#include <cstdio>
using namespace std;
int T,a,b;
int main()
{
	scanf("%d",&T);
	for(int x=0; x<T; x++)
	{
		scanf("%d %d",&a,&b);
		printf("Case #%d: %d + %d = %d\n",x+1,a,b,a+b);
	}
}