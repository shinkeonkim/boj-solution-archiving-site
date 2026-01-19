#include <iostream>
#include <string>
using namespace std;
string a;
int Sum=0;
int f(char k)
{
	switch(k)
	{
		case 'A':
		case 'B':
		case 'C':
			return 3;
		case 'D':
		case 'E':
		case 'F':
			return 4;
		case 'G':
		case 'H':
		case 'I':
			return 5;
		case 'J':
		case 'K':
		case 'L':
			return 6;
		case 'M':
		case 'N':
		case 'O':
			return 7;
		case 'P':
		case 'Q':
		case 'R':
		case 'S':
			return 8;
		case 'T':
		case 'U':
		case 'V':
			return 9;
		case 'W':
		case 'X':
		case 'Y':
		case 'Z':
			return 10;
	}
}
int main()
{
	cin>>a;
	for(int x=0; x<a.length(); x++)
	{
		Sum+=f(a[x]);
	}
	cout<<Sum;
}