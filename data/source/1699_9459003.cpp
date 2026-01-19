#include <iostream>

using namespace std;

#define Mx 9999999

int N,ar[1100000];

int main() {
	cin >> N;
	ar[0]=0;
	for(int x=1; x<=100000; x++) ar[x]=Mx;
	for(int x=0; x<=N; x++) {
		if(ar[x]!=Mx) {
			for(int y = 1; y <= 330; y++) {
				if(ar[x + y * y]>ar[x]+1) {
					ar[x + y * y] = ar[x] + 1;
				}
			}
		}
	}
	cout << ar[N];
}