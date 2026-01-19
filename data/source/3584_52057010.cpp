#include <bits/stdc++.h>

using namespace std;

int tc;
int n, a, b, qa, qb;
int root = -1;
int parent[11000];
int depth[11000];
vector <int> edges[11000];

void init() {
	fill(depth, depth + n + 1, 0);
	fill(parent, parent + n + 1, 0);

	for(int i = 1; i <= n; i++) {
		edges[i].clear();
	}
}

void prepare_root() {
	root = -1;

	for(int i = 1; i <= n; i++) {
		if(parent[i] != 0) continue;

		root = i;
	}
}

void prepare_depth(int here, int d) {
	depth[here] = d;
	
	for(auto there : edges[here]) {
		prepare_depth(there, d + 1);
	}
}

int main() {
	cin >> tc;
	
	while(tc--) {

		cin >> n;
		
		init();
		
		for(int i = 1; i < n; i++) {
			cin >> a >> b;
			
			parent[b] = a;
			edges[a].push_back(b);
		}
		
		cin >> qa >> qb;
		
		depth[0] = -1;
		prepare_root();
		prepare_depth(root, 0);
		
		while(qa != qb) {
			if(depth[qa] == depth[qb]) {
				qa = parent[qa];
				qb = parent[qb];
			} else if(depth[qa] > depth[qb]) {
				qa = parent[qa];
			} else {
				qb = parent[qb];
			}
			
		}
		
		cout << qa << "\n";
	}
}