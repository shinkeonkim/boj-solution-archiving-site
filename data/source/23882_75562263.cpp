#include <bits/stdc++.h>

#define for1(s,n) for(int i = s; i < n; i++)
#define for1j(s, e) for(int j = s; j < e; j++)

#define foreach(k) for(auto i : k)
#define foreachj(k) for(auto j : k) 
#define pb(a) push_back(a)
#define sz(a) a.size()
#define all(vct) vct.begin(), vct.end()
#define uniq(vct) sort(all(vct));vct.erase(unique(all(vct)), vct.end())
#define fi first
#define se second

using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int uint;

typedef vector <int> iv1;
typedef vector <vector<int> > iv2;

typedef vector <ll> llv1;
typedef vector <vector <ll> > llv2;

typedef vector <ull> ullv1;
typedef vector <vector <ull> > ullv2;

typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef pair<double, double> pdd;
typedef pair<string, string> pss;


ll N, K;
llv1 ar;

void solve() {
	cin >> N >> K;

	for1(0, N) {
		ll a;
		cin >> a;
		ar.push_back(a);
	}

	int cnt = 0;

	for(int last = N - 1; last >= 1; last--) {
		ll mx_idx = last;

		for(int i = 0; i <= last; i++) {
			if(ar[i] > ar[mx_idx]) {
				mx_idx = i;
			}
		}

		if(last != mx_idx) {
			int tmp = ar[last];
			ar[last] = ar[mx_idx];
			ar[mx_idx] = tmp;
			cnt++;

			if(cnt == K) {
				for1(0, N) {
					cout << ar[i] << " ";
				}
				return;
			}
		}
	}

	cout << -1;
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);

  int tc = 1;

  while(tc--) {
    solve();
  }
}