#include <bits/stdc++.h>

using namespace std;

int N, M;
string ar[660];
int sy, sx;
int ans = 0;
bool check[660][660];

int dy[] = { 0, 0, 1, -1 };
int dx[] = { 1, -1, 0, 0 };

void dfs(int hy, int hx) {
	if(check[hy][hx]) return;
	
	check[hy][hx] = true;
	
	if(ar[hy][hx] == 'P') ans++;
	
	for(int d = 0; d < 4; d++) {
		int ny = hy + dy[d];
		int nx = hx + dx[d];
		
		if(ny < 0 || nx < 0 || ny >= N || nx >= M) continue;
		
		if(ar[ny][nx] == 'X') continue;
		
		dfs(ny, nx);
	}
}

int main() {
	cin >> N >> M;
	
	for(int i = 0; i < N; i++) {
		cin >> ar[i];
		
		for(int j = 0; j < M; j++) {
			if(ar[i][j] == 'I') {
				sy = i;
				sx = j;
			}
		}
	}
	
	dfs(sy, sx);
	
	if(ans) {
		cout << ans;
	} else {
		cout << "TT";
	}
}
