#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef vector<ll> llv1;

ll N, ans;
bool D[11000];

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	
	cin >> N;
	
	while(N >= 0 && !D[N]) {
		D[N] = true; 
		ans++;
	
		N = (N % 1000) / 10;
		N *= N;
	}
	
	cout << ans;
}