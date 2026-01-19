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
string a[33];
string ar[33];
ll D[330][2200];

ll f(ll idx, ll state) {
	if(idx == N * M) {
		return state == 0 ? 0 : -INF;
	}
	
	if(idx > N*M) return -INF;
	
	ll &ans = D[idx][state];
	
	if(ans != -1) return ans;
	
	ll i = idx / M;
	ll j = idx % M;
	
	if(ar[i][j] == '1') return ans = f(idx + 1, state >> 1) + 1;
	
	ans = f(idx + 1, state >> 1);
	
	if((state & 1) == 0) {
		ans = max(ans, f(idx + 1, state >> 1) + 1);
	}
	
	if(i != N - 1 && j != M - 1 && (state & 1) == 0 && (state & 2) == 0) {
		if(ar[i+1][j] == '.' && ar[i][j+1] == '.' && ar[i+1][j+1] == '.') {
			ans = max(ans, f(idx + 2, (state >> 2) | (3 << (M - 2))) + 16);
		}
	}
		
	return ans;
}


int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);

	cin >> N >> M;
	
	for1(0, N) {
		cin >> a[i];
	}
	
	for1(0, M) {
		for1j(0, N) {
			ar[i] += a[j][i]; 
		}
	}
	
	swap(N, M);
	
	memset(D, -1, sizeof(D));
	
	cout << f(0, 0);
}