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

ll tc, M, N, x, y;

ll gcd(ll a, ll b) {
	return b > 0 ? gcd(b, a % b) : a;
}

ll lcm(ll a, ll b) {
	return a / gcd(a, b) * b;
}

int main() {
  ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	
	cin >> tc;
	while(tc--) {
		cin >> M >> N >> x >> y;
		
		ll mx = lcm(M, N);
		
		bool flag = false;
		
		while(x <= mx && y <= mx) {
			if(x == y) {
				flag = true;
				break;
			}
			
			if(x < y) {
				x += M;
			} else {
				y += N;
			}
		}
		
		if(flag) {
			cout << x;
		} else {
			cout << -1;
		}
		cout << "\n";
	}
}