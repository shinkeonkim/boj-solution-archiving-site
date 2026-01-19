#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

ll N, M, K;
ll ar[110][110];
ll D[110];

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);

	cin >> N >> M >> K;
	
	for(int i = 0; i < N; i++)
		for(int j = 0; j < M; j++)
			cin >> ar[i][j];

	int ans = 0;
	int cnt = 0;
	
	for(int j = 0; j < M; j++) {
		if(ans) break;
		cnt++;
	
		for(int i = 0; i < N; i++) {
			if(ans) break;
			D[i] += ar[i][j];
			
			if(D[i] >= K) ans = i + 1;
		}
	}
	
	cout << ans << " " << cnt;
}