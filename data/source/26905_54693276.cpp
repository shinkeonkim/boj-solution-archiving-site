#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef vector<ll> llv1;

ll N, ans;
ll ar[1100];

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	
	cin >> N;
	for(int i = 0; i < N; i++) {
		cin >> ar[i];
	}
	
	for(int i = 0; i < N; i++) {
		for(int j = i % 2; j < N; j += 2) {
			if(ar[j] > ar[j + 1] && j + 1 < N) {
				ans++;

				ar[j] = ar[j + 1] ^ ar[j];
				ar[j + 1] = ar[j + 1] ^ ar[j];
				ar[j] = ar[j + 1] ^ ar[j];
			}
		}
	}
	
	cout << ans;
}