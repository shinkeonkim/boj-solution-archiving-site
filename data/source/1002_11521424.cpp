#include <iostream>
using namespace std;
int T;
long long int x1,y1,r1,x2,y2,r2,k;
int main()
{
	cin>>T;
	for(int x=0; x<T; x++)
	{
		cin>>x1>>y1>>r1>>x2>>y2>>r2;
		if(r2>r1) // r1이 무조건 크거나 같게 설정 
		{
			k=x1; x1=x2; x2=k;
			k=y1; y1=y2; y2=k;
			k=r1; r1=r2; r2=k;
		}
		if(x1==x2&&y1==y2&&r1==r2) //완전히 일치하는 경우  무한대 
		{
			cout<<-1;
		}
		else if(x1==x2&&y1==y2) // 중심이 같지만 반지름이 다른경우 0 
		{
			cout<<0;
		} 
		else 
		{
			long long int D=((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)); // 중심과 중심 사이의 거리의 제곱을 D라 하자 
			
			if(D<r1*r1) //반지름이 작은 r2를 가진 원의 중심이 r1을 가진원의 내부에 있는 경우 
			{
				if(D==((r1-r2)*(r1-r2))) cout<<1;
				else if(D<((r1-r2)*(r1-r2))) cout<<0;
				else cout<<2; 
			}
			else if(D==r1*r1) //반지름이 작은 r2를 가진 원의 중심이 r1을 가진원에 걸쳐 있는 경우
			{
				cout<<2;
			}
			else//반지름이 작은 r2를 가진 원의 중심이 r1을 가진 원의 외부에 있는 경우
			{
				if(D>(r1+r2)*(r1+r2)) cout<<0;
				else if(D==(r1+r2)*(r1+r2)) cout<<1;
				else if(D<(r1+r2)*(r1+r2)) cout<<2;	
			}
		}
		cout<<endl;
	}
}