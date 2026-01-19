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

ll N, ans = 1000000000LL;
ll score[22][22];
bool check[22];

void g() {
	int ret[] = {0, 0};
	
	for(int i = 0; i < N; i++) {
		for(int j = i + 1; j < N; j++) {
			if(check[i] == check[j]) {
				ret[check[i]] += score[i][j] + score[j][i];
			}
		}
	}
	
	ans = min(ans, (ll)abs(ret[0] - ret[1]));
}

void f(int idx) {
	for1(0, 2) {
		check[idx] = i;
		
		if(idx == N - 1) {
			g();
		} else {
			f(idx + 1);
		}
	}
}

int main() {
  ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	
	cin >> N;
	for1(0, N) {
		for1j(0, N) {
			cin >> score[i][j];
		}
	}
	
	f(0);
	
	cout << ans;
}