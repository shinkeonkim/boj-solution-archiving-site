#include <iostream>
using namespace std;
int main()
{
	for(int x=0; x<3; x++)
	{
		int Sum=0,a;
		for(int y=0; y<4; y++)
		{
			cin>>a;
			Sum+=a;
		}
		switch(Sum)
		{
			case 0: cout<<"D";break;
			case 1: cout<<"C";break;
			case 2: cout<<"B";break;
			case 3: cout<<"A";break;
			case 4: cout<<"E";break;
		}
		cout<<endl; 
	}
}