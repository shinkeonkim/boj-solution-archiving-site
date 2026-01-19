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

ll N, M;
ll D[330][22000];

ll f(ll idx, ll state) {
	if(idx == N * M && state == 0) {
		return 1;
	}
	
	if(idx >= N * M) {
		return 0;
	}
	
	if(D[idx][state] >= 0) return D[idx][state];\
	
	ll &ret = D[idx][state];
	
	ret = 0;
	
	if(state & 1) {
		return ret = f(idx + 1, state >> 1) % 9901;
	}
	
	if((idx + 1) % M != 0 && (state & 2) == 0) {
		ret += f(idx + 2, (state >> 2));
	}
	
	ret += f(idx + 1, (state >> 1) | (1 << (M - 1)));
	ret %= 9901;

	return ret;
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);

	cin >> N >> M;
	
	memset(D, -1, sizeof(D));
	
	cout << f(0, 0);
}