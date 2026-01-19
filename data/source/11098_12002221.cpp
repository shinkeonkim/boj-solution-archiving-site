#include <iostream> 
#include <string>
using namespace std;
int N,P,C,Max=-1;
string Max_name;
string name;
int main()
{
	cin>>N;
	for(int i=0; i<N; i++)
	{
		cin>>P; 
		Max=-1;
		for(int x=0; x<P; x++)
		{
			cin>>C>>name;
			if(C>Max)
			{
				Max=C;
				Max_name=name;
			}
		}
		cout<<Max_name<<endl;
	}
}