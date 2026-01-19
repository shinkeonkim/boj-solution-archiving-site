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

struct st {
	ll x, y;
};

st ar[8];
ll D[8][8];

ll f(st a, st b) {
	return llabs(a.x - b.x) + llabs(a.y - b.y);
}

int main() {
  ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	
	for1(0, 8) {
		cin >> ar[i].x >> ar[i].y;
	}
	
	for1(0, 8) {
		for1j(0, 8) {
			D[i][j] = f(ar[i], ar[j]);
			if(i >= 2 && i / 2 == j / 2) D[i][j] = min(10ll, D[i][j]);
		}
	}
	
	for1(0, 8) {
		for1j(0, 8) {
			for(int k = 0; k < 8; k++) {
				if(D[j][k] > D[j][i] + D[i][k]) D[j][k] = D[j][i] + D[i][k];
			}
		}
	}
	
	cout << D[0][1];
}