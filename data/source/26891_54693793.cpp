#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef vector<ll> llv1;

ll N;
ll ans;

ll mn(ll a, ll b) {
	return a < b ? a : b;
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);

	cin >> N;
	
	ans = 2 * (N + 1);
	
	for(int i = 2; i * i <= N; i++) {
		int k = N / i;
		if(N % i > 0) k += 1;

		ans = mn(ans, (i + 1) * (k + 1));
	}
	
	cout << ans;
}