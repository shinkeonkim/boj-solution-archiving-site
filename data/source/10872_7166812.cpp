#include <iostream>
using namespace std;
int N,F=1;
int main(){
	cin>>N;
	for(int x=1; x<=N; x++)F*=x;
	cout<<F;
} 