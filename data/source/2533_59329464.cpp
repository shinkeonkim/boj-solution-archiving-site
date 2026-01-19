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

ll N, a, b;
llv1 adj[1100000];
ll D[1100000][2];

ll dfs(int here, int stat, int par) {
	if(D[here][stat]) return D[here][stat];
	
	ll ret = 0;
	
	if(stat) ret++;
		
	for(auto there : adj[here]) {
		if(there == par) continue;
		
		if(stat) {
			ret += min(dfs(there, stat, here), dfs(there, 1 - stat, here));	
		} else {
			ret += dfs(there, 1 - stat, here);
		}
	}
	
	return D[here][stat] = ret;
}

int main() {
  ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	
	cin >> N;
	
	for1(0, N - 1) {
		cin >> a >> b;
		adj[a].push_back(b);
		adj[b].push_back(a);
	}
	
	ll ans = min(dfs(1, 0, -1), dfs(1, 1, -1));
	
	cout << ans;
}