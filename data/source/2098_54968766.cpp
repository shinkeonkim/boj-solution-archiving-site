#include <bits/stdc++.h>

#define for1(s,n) for(int i = s; i < n; i++)
#define for1j(s,n) for(int j = s; j < n; j++)
#define foreach(k) for(auto i : k)
#define foreachj(k) for(auto j : k)
#define pb(a) push_back(a)
#define sz(a) a.size()

#define INF (ll)1000000000

using namespace std;
typedef unsigned long long ull;
typedef long long ll;
typedef vector <int> iv1;
typedef vector <vector<int> > iv2;
typedef vector <ll> llv1;
typedef unsigned int uint;
typedef vector <ull> ullv1;
typedef vector <vector <ull> > ullv2;

ll n;
ll weights[22][22];
ll D[110000][22];

// D[S][i] = 최소비용
// S : 현재까지 방문한 도시의 상태값
// i : 마지막으로 방문한 도시

ll min(ll a, ll b) {
	return a < b ? a : b;
}

int main() {
  ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	
	cin >> n;
	
	for1(0, n) {
		for1j(0, n) {
			cin >> weights[i][j];
		}
	}
	
	for1(0, 1 << n) {
		for1j(0, n) {
			D[i][j] = INF;
		}
	}
	
	D[1][0] = 0;
	
	for(int i = 0; i < (1 << n); i++) {
		for(int j = 1; j < n; j++) {
			if(i & (1 << j)) {
				// j를 마지막으로 방문한 경우
				
				for(int k = 0; k < n; k++) {
					// k: j 전에 방문한 지점

					if (k != j && (i & (1 << k)) && weights[k][j] && D[i - (1 << j)][k] != INF) {
						D[i][j] = min(D[i][j], D[i - (1 << j)][k] + weights[k][j]);
					}
				}
			}
		}
	}
	
	ll ans = INF;
	
	for(int i = 0; i < n; i++) {
		if(weights[i][0])
			ans = min(ans, D[(1 << n) - 1][i] + weights[i][0]);
	}
	
	cout << ans;
}