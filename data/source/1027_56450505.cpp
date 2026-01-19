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

ll N;
ll ar[55];
ll cnt[55];

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	
	cin >> N;	
	
	for1(0, N) cin >> ar[i];
	
	for1(0, N) {
		for1j(i+1, N) {
			bool flag = true;
			for(ll k = i + 1; k < j; k++) {
				if((ar[j] - ar[i]) * (k - i) <= (ar[k] - ar[i]) * (j - i)) {
					flag = false;
					break;
				}
			}
			
			if(flag) {
				cnt[j]++;
				cnt[i]++;
			}
		}
	}
	
	ll ans = cnt[0];
	
	for1(0, N) {
		ans = max(ans, cnt[i]);
	}
	
	cout << ans;
	
	
}