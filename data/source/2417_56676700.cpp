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

ull N;
ull s = 0;
ull e;

ull ans;

int main() {
  ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	
	cin >> N;
	
	if(N == 0) {
		cout << 0;
		return 0;
	}
	
	ans = N;
	e = 4294967296ULL;
	
	while(s <= e) {
		ull mid = (s + e) / 2;
		
		if(mid * mid >= N) {
			if(mid < ans) ans = mid;
			e = mid - 1;
		} else {
			s = mid + 1;
		}
	}
	
	cout << ans;
}