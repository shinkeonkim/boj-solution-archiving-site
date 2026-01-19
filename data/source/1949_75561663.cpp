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
int dp[11000][2];
int weight[11000];

int f(int node, int status, int par) {
	if(dp[node][status]) return dp[node][status];

	int ret = 0;

	if(status == 1) {
		ret += weight[node];
	}

	for(auto edge : edges[node]) {
		if(edge == par) continue;

		if(status == 1) {
			ret += f(edge, 0, node);
		} else {
			ret += max(f(edge, 1, node), f(edge, 0, node));
		}
	}
	return dp[node][status] = ret;
}


void solve() {
	cin >> N;
	for1(1, N + 1) {
		cin >> weight[i];
	} 

	for1(0, N - 1) {
		ll a, b;
		cin >> a >> b;

		edges[a].push_back(b);
		edges[b].push_back(a);
	}
	
	int ans = f(1, 1, 0);
	ans = max(ans, f(1, 0, 0));

	cout << ans;


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