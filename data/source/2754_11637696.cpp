#include <iostream>
using namespace std;
char a,b;
int main()
{
	cin>>a;
	if(a=='F') cout<<"0.0";
	else
	{
		cin>>b;
		switch(a)
		{
			case 'A':
				if(b=='+') cout<<"4.3";
				if(b=='0') cout<<"4.0";
				if(b=='-') cout<<"3.7";
				break;
			case 'B':
				if(b=='+') cout<<"3.3";
				if(b=='0') cout<<"3.0";
				if(b=='-') cout<<"2.7";
				break;
			case 'C':
				if(b=='+') cout<<"2.3";
				if(b=='0') cout<<"2.0";
				if(b=='-') cout<<"1.7";
				break;
			case 'D':
				if(b=='+') cout<<"1.3";
				if(b=='0') cout<<"1.0";
				if(b=='-') cout<<"0.7";
				break;
		}
	}
	
}