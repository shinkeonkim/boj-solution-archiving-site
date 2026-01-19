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

int N;
iv1 adj[110];
bool check[110];

bool dfs(int here) {
	if(check[here]) return false;
	
	check[here] = true;
	
	for(auto there : adj[here]) {
		bool ret = dfs(there);
		
		if(!ret) return false;
	}
	
	check[here] = false;
	
	return true;
}


int main() {
  ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	
	cin >> N;
	
	for(int i = 1; i < N; i++) {
		int cnt, a;
		
		cin >> cnt;
		
		for(int j = 0; j < cnt; j++) {
			cin >> a;
			
			adj[i].push_back(a);
		}
	}
	
	bool ret = dfs(1);
	
	cout << (ret ? "NO CYCLE" : "CYCLE");
}