#include <iostream>
using namespace std;
int T,N,x1,y1,x2,y2,x3,y3,r,Ans,Cnt;
int main()
{
	cin>>T;
	for(int t=0; t<T; t++)
	{
		Ans=0;
		cin>>x1>>y1>>x2>>y2>>N;
		for(int y=0; y<N; y++)
		{
			Cnt=0;
			cin>>x3>>y3>>r;
			if(r*r>((x1-x3)*(x1-x3)+(y1-y3)*(y1-y3)))Cnt++;
			if(r*r>((x2-x3)*(x2-x3)+(y2-y3)*(y2-y3)))Cnt++;
			if(Cnt==1) Ans++;
		}
		cout<<Ans<<endl;
	}	
} 