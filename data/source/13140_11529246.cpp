#include <iostream>
using namespace std;
int N,A,B,h,w,e,l,o,r,d;
bool f()
{
	if(h!=w&&h!=e&&h!=l&&h!=o&&h!=r&&h!=d)
	{
		if(w!=e&&w!=l&&w!=o&&w!=r&&w!=d)
		{
			if(e!=l&&e!=o&&e!=r&&e!=d)
			{
				if(l!=o&&l!=r&&l!=d)
				{
					if(o!=r&&o!=d)
					{
						if(r!=d)
						{
							return true;
						}
					}
				}
			}
		}
	}
	return false;
	
	
}
int main()
{
	cin>>N;
	
	for(h=1; h<=9; h++)
	for(w=1; w<=9; w++)
	for(e=0; e<=9; e++)
	for(l=0; l<=9; l++)
	for(o=0; o<=9; o++)
	for(r=0; r<=9; r++)
	for(d=0; d<=9; d++)
	{
		A=h*10000+e*1000+l*110+o;
		B=w*10000+o*1000+r*100+l*10+d;
		if(A+B==N&&f())
		{
			cout<<"  "<<A<<endl;
			cout<<"+ "<<B<<endl;
			cout<<"-------\n";
			if(N>999999);
			else if(N>99999) cout<<" ";
			else if(N>9999) cout<<"  ";
			else if(N>999) cout<<"   ";
			cout<<N;
			return 0;
			 
		}
	}
	cout<<"No Answer";
}