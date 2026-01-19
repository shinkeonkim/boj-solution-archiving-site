#include <bits/stdc++.h>

#define for1(s,n) for(int i = s; i < n; i++)
#define for1j(s,n) for(int j = s; j < n; j++)
#define foreach(k) for(auto i : k)
#define foreachj(k) for(auto j : k)
#define pb(a) push_back(a)
#define sz(a) a.size()
#define INF 1e8

using namespace std;
typedef pair <int, int> pii;

int N;
vector<int> edges[110000];
int order[110000];
bool chk[110000];

int main() {
  ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	
	cin >> N;
	for1(0, N - 1) {
		int a, b;
		cin >> a >> b;
		edges[a].push_back(b);
		edges[b].push_back(a);
	}
	
	for1(0, N) {
		int a;
		cin >> a;
		order[a] = i;
	}
	
	queue<int> Q;
	Q.push(1);
	int crt = 0;
	
	while(!Q.empty()) {
		int f = Q.front(); Q.pop();
		
		if(crt != order[f]) {
			cout << 0;
			return 0;
		}
		
		chk[f] = true;
		
		crt++;
		
		vector <pii> v;
		
		for(int nxt : edges[f]) {
			if(chk[nxt]) continue;
			
			v.push_back({ order[nxt], nxt });
		}
		
		sort(v.begin(), v.end());
		
		for(auto nxt : v) {
			Q.push(nxt.second);
		}
	}
	
	cout << 1;

}