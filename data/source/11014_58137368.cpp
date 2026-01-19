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

int N, M;

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

int to_num(int y, int x) {
	return y * M + x;
}

int main() {
  ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	
	int tc;
	int dy[] = {0, -1, -1};
	int dx[] = {-1, 1, -1};
	
	cin >> tc;
	
	while(tc--) {		
		cin >> N >> M;
		
		MVC mvc(6500);
		string ar[N];
		
		for1(0, N) {
			cin >> ar[i];
		}
		
		int total = 0;
		
		for1(0, N) {
			for1j(0, M) {
				if(ar[i][j] == 'x') {
					continue;
				}
				total++;
				
				for(int d = 0; d < 3; d++) {
					int ny = i + dy[d];
					int nx = j + dx[d];
					
					if(ny < 0 || nx < 0 || ny >= N || nx >= M) continue;
					if(ar[ny][nx] == 'x') continue;
					
					if(j % 2 == 0) {
						mvc.add_edge(to_num(i, j), to_num(ny, nx));
					} else {
						mvc.add_edge(to_num(ny, nx), to_num(i, j));
					}
					
				}
			}
		}
		
		cout << total - mvc.flow() << "\n";
	}
}