#include <iostream>
using namespace std;
int N,M,Cnt;
int main()
{
	cin>>N>>M;
	for(int x=1; x<N; x++)
	{
		if(x==1||x==3||x==5||x==7||x==8||x==10||x==12) Cnt+=31;
		else if(x==2) Cnt+=28;
		else if(x==4||x==6||x==9||x==11)Cnt+=30;
	}
	Cnt+=M;
	switch(Cnt%7)
	{
		case 0:
			cout<<"SUN";
			break;
		case 1:
			cout<<"MON";
			break;
		case 2:
			cout<<"TUE";
			break;
		case 3:
			cout<<"WED";
			break;
		case 4:
			cout<<"THU";
			break;
		case 5:
			cout<<"FRI";
			break;
		case 6:
			cout<<"SAT";
			break;
	}
}