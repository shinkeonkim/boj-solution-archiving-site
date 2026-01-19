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

struct MVC {
	int n;
	vector<vector<int>> graph;
	vector<bool> chk;
	vector<int> prev;
	
	MVC(int n) : n(n) {
		graph.resize(n);
		chk.resize(n);
		prev.resize(n, -1);
	};
	
	void add_edge(int u, int v) {
		graph[u].push_back(v);
	}
	
	bool dfs(int x) {
		if(x == -1) return true;
		
		for(int nxt : graph[x]) {
			if(chk[nxt]) continue;
			
			chk[nxt] = true;
			
			if(dfs(prev[nxt])) {
				prev[nxt] = x;
				return true;
			}
		}
		
		return false;
	}
	
	int flow() {
		int ans = 0;
		for(int i = 0; i < n; i++) {
			fill(chk.begin(), chk.end(), false);
			
			if(dfs(i)) ans += 1;
		}
		return ans;
	}
};


int main() {
  ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	
	int N, K, a, b;
	
	cin >> N >> K;
	
	MVC mvc(N);
	
	for1(0, K) {
		cin >> a >> b;
		
		mvc.add_edge(a - 1, b - 1);
	}
	
	cout << mvc.flow();
}