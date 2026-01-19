#include <bits/stdc++.h>

#define for1(s,n) for(int i = s; i < n; i++)
#define for1j(s,n) for(int j = s; j < n; j++)
#define foreach(k) for(auto i : k)
#define foreachj(k) for(auto j : k)
#define pb(a) push_back(a)
#define sz(a) a.size()

using namespace std;
typedef unsigned long long ull;
typedef long long ll;
typedef vector <int> iv1;
typedef vector <vector<int> > iv2;
typedef vector <ll> llv1;
typedef unsigned int uint;
typedef vector <ull> ullv1;
typedef vector <vector <ull> > ullv2;

int A, B;
int ar[11000000];

int main() {
  ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	
	cin >> A >> B;
	
	ar[0] = ar[1] = 1;
	
	for1(2, 10000000) {
		ar[i] = (ar[i-1] + ar[i-2]) % 10;
	}
	
	for1(A - 1, B) {
		cout << ar[i];
	}	
}