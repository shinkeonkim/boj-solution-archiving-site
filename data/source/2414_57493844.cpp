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

struct MF {
	int n;
	int source, sink;
	
	vector<vector<int>> graph;
	vector<bool> chk;
	vector<int> prev;
	
	MF(int n) : n(n) {
		graph.resize(n);
		chk.resize(n);
		prev.resize(n, -1);
	};
	
	void add_edge(int u, int v) {
		graph[u].push_back(v);
	}
	
	bool dfs(int x) {
		if(x == -1) return true;
		
		for(int next : graph[x]) {
			if(chk[next]) continue;
			
			chk[next] = true;
			
			if(dfs(prev[next])) {
				prev[next] = x;
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

int n, m;
string ar[55];
int row[55][55];
int col[55][55];

int r = 1;
int c = 1;

int main() {
  ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	
	cin >> n >> m;
	
	for1(0, n) {
		cin >> ar[i];
	}
	
	for1(0, n) {
		for1j(0, m) {
			if(ar[i][j] == '*' ) {
				if(j == 0 || ar[i][j - 1] == '.') {
					row[i][j] = r++;
				} else if(ar[i][j - 1] == '*') {
					row[i][j] = row[i][j - 1];
				}
			}
		}
	}
	
	for1j(0, m) {
		for1(0, n) {
			if(ar[i][j] == '*' ) {
				if(i == 0 || ar[i - 1][j] == '.') {
					col[i][j] = c++;
				} else if(ar[i - 1][j] == '*') {
					col[i][j] = col[i- 1][j];
				}
			}
		}
	}
	
	MF mf(max(r, c));
	
	for1(0, n) {
		for1j(0, m) {
			if(row[i][j] && col[i][j]) {
				mf.add_edge(row[i][j], col[i][j]);
			}
		}
	}
	
	cout << mf.flow();
}