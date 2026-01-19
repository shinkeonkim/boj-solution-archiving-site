#include <iostream>
#include <algorithm>
using namespace std;
int A,B,C,D,E,F;
int main()
{
	cin>>A>>B>>C>>D>>E>>F;
	cout<<A+B+C+D+max(E,F)-min(A,min(B,min(C,D)));
}