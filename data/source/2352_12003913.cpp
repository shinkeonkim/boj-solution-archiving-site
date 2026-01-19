#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int N,S,A;
vector <int> V;

int main() {
	V.push_back(-1);	
	cin>>N;
	for(int x=0; x<N; x++) {
		cin>>A;
		if(V.back()<A) {
			V.push_back(A);
			S++;
		} else {
			auto it=lower_bound(V.begin(),V.end(),A);
			*it=A;
		}
	}
	cout << S;
} 