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

int C;
int N, M;
string ar[11];

int d[11][1 << 10];

bool is_in_state(int state, int i) {
	return (state & (1 << i)) > 0;
}

bool check(int row, int state) {
	if(row < 0) return true;
	
	for(int j = 0; j < M - 1; j++) {
		if(is_in_state(state, j) && is_in_state(state, j + 1)) return false;
	}
	
	for(int j = 0; j < M; j++) {
		if(ar[row][j] == 'x' && is_in_state(state, j)) return false;
	}
	
	return true;
}


int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	
	cin >> C;
	
	while(C--) {
		cin >> N >> M;
		
		for1(0, N) cin >> ar[i];
		
		memset(d, 0, sizeof(d));
		
		for(int row = 0; row < N; row++) {
			for(int state = 0; state < (1 << M); state++) {
				if(!check(row, state)) continue;
				
				for(int prev_state = 0; prev_state < (1 << M); prev_state++) {
					if(!check(row - 1, prev_state)) continue;
					
					int cnt = 0;
					bool flag = true;
					
					for(int i = 0; i < M; i++) {
						if(is_in_state(state, i)) {
							cnt++;
							
							if(i - 1 >= 0 && is_in_state(prev_state, i - 1)) flag = false;
							if(i + 1 < M && is_in_state(prev_state, i + 1)) flag = false;
						}
					}
					
					if(!flag) continue;
					
					if(row == 0) d[row][state] = max(d[row][state], cnt);
					else d[row][state] = max(d[row][state], d[row - 1][prev_state] + cnt);
				}
			}
		}
		
		int ans = 0;
		
		for(int state = 0; state < (1 << M); state++) {
			ans = max(ans, d[N - 1][state]);
		}
		
		cout << ans << "\n";
	}
}