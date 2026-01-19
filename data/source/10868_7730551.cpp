#include <iostream>
using namespace std;

struct st{
	int a,b;
};

const int Mx=1100000000;
int N,M,ar[110000],tree[440000];
st query[110000];

int MakeTree(int left, int right, int idx)
{
	if(left==right)
	{
		return tree[idx]=ar[left];
	}
	else
	{
		int mid=(left+right)/2;
		int L=MakeTree(left,mid,2*idx);
		int R=MakeTree(mid+1,right,2*idx+1);
		if(L<R) return tree[idx]=L;
		return tree[idx]=R;
	}
}
int Find(int left,int right,int idx,int a,int b)
{
	if(b<left||right<a) return Mx;
	if(a<=left&&right<=b) return tree[idx];
	
	int mid=(left+right)/2;
	int L=Find(left,mid,2*idx,a,b);
	int R=Find(mid+1,right,2*idx+1,a,b);

	if(L<R) return L;
	return R;
}
int main()
{
	cin>>N>>M;
	for(int x=1; x<=N; x++) scanf("%d",&ar[x]);
	for(int x=1; x<=M; x++) scanf("%d %d",&query[x].a,&query[x].b);
	MakeTree(1,N,1);
	for(int x=1; x<=M; x++)
	{
		printf("%d\n",Find(1,N,1,query[x].a,query[x].b));
	}
	
}