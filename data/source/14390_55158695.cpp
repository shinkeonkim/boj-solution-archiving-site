#include <bits/stdc++.h>

#define for1(s,n) for(int i = s; i < n; i++)
#define for1j(s,n) for(int j = s; j < n; j++)
#define foreach(k) for(auto i : k)
#define foreachj(k) for(auto j : k)
#define pb(a) push_back(a)
#define sz(a) a.size()
#define INF 1000000000

using namespace std;
typedef unsigned long long ull;
typedef long long ll;
typedef vector <int> iv1;
typedef vector <vector<int> > iv2;
typedef vector <ll> llv1;
typedef unsigned int uint;
typedef vector <ull> ullv1;
typedef vector <vector <ull> > ullv2;

ll N, M;
string ar[11];
ll D[11][1100]; // row, state;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	
	cin >> N >> M;
	
	for1(1, N + 1) cin >> ar[i];
	
	memset(D, -1, sizeof(D));
	
	D[0][0] = 0;
	
	for(int row = 1; row <= N; row++) {
		for(int prev = 0; prev < (1 << M); prev++) {
			if(D[row - 1][prev] == -1) continue;
			// 이전 행이 불가능한 경우는 스킵한다. 
			for(int crt = 0; crt < (1 << M); crt++) {
				int cnt = 0;
				int last = -10;
				
				for(int k = 0; k < M; k++) {
					if(ar[row][k] == '#') continue;
				
					if(crt & (1 << k)) {
						if(row == 1 || (prev & (1 << k)) == 0 || ar[row - 1][k] == '#') cnt++;
						// 첫 행인 경우
						// 이전 행에서 가로를 놓은 경우
						// 이전 행이 막힌 칸인 경우
					} else {
						if(last + 1 != k) cnt ++;
						last = k;
					}
				}
				
				if(D[row][crt] == -1 || D[row][crt] > D[row - 1][prev] + cnt) {
					D[row][crt] = D[row - 1][prev] + cnt;
				}
			}
		}
	}
	
	ll ans = -1;
	
	for(int i = 0; i < (1 << M); i++) {
		if(ans == -1 || ans > D[N][i]) ans = D[N][i];
	}
	
	cout << ans << "\n";
}
