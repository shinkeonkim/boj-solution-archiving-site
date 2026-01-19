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

ll tc;
ll N;
ll ar[550];
ll sm[550];
ll D[550][550];

ll f(ll s, ll e) {
	if(s < 0 || e >= N || s > e) return INF;
	
	ll &ret = D[s][e];
	
	if(ret != INF) return ret;
	
	if(s == e) return ret = 0;
	
	if(s + 1 == e) return ret = ar[s] + ar[e];
	
	for1(s, e) {
		ret = min(ret, f(s, i) + f(i + 1, e));
	}
	
	ret += sm[e + 1] - sm[s];

	return ret;
}


int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);

	cin >> tc;
	
	while(tc--) {
		cin >> N;
	
		for1(0, N) {
			cin >> ar[i];
			
			for1j(0, N) {
				D[i][j] = INF;
			}
		}
		
		sm[1] = ar[0];
		
		for1(1, N) {
			sm[i + 1] = sm[i] + ar[i];
		}

		cout << f(0, N - 1) << "\n";
	}
	
}