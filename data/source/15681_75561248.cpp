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

ll N, R, Q;
llv1 edges[110000];
int chk[110000];

int f(int node, int par) {
	int ret = 1;

	for(auto edge : edges[node]) {
		if(edge == par) continue;

		ret += f(edge, node);
	}
	return chk[node] = ret;
}

void solve() {

	cin >> N >> R >> Q;

	for1(0, N - 1) {
		ll a, b;
		cin >> a >> b;

		edges[a].push_back(b);
		edges[b].push_back(a);
	}

	chk[R] = f(R, -1);
	
	for1(0, Q) {
		int query;

		cin >> query;

		cout << chk[query] << "\n";
	}

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