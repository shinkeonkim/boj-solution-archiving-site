#include <iostream>
using namespace std;
int N,Min=999999999;
int main()
{
	cin>>N;
	for(int x=0; x<=1000; x++)
	{
		for(int y=0; y<1667; y++)
		{
			if(x*5+y*3==N&&Min>x+y)Min=x+y;
		}
	}
	if(Min==999999999)cout<<"-1";
	else cout<<Min;
}