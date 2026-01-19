#include <bits/stdc++.h>

#define for1(s,n) for(int i = s; i < n; i++)
#define for1j(s,n) for(int j = s; j < n; j++)

using namespace std;

struct Node {
	int y, x;
	int py, px;
};

int N, M;
string ar[55];
bool chk[55][55];
int dy[] = {0, 0, 1, -1};
int dx[] = {1, -1, 0, 0};

bool bfs() {	
	queue<Node> Q;

	for1(0, N) {
		for1j(0, M) {
			if(chk[i][j]) {
				continue;
			}
			
			Q.push({i, j, -1, -1});
			
			while(!Q.empty()) {
				auto f = Q.front();
				Q.pop();
				
				if(chk[f.y][f.x]) return true;
				
				chk[f.y][f.x] = true;
				
				for(int d = 0; d < 4; d++) {
					int ny = f.y + dy[d];
					int nx = f.x + dx[d];
					
					if(ny < 0 || nx < 0 || ny >= N || nx >= M) continue;
					if(ny == f.py && nx == f.px) continue;
					if(ar[f.y][f.x] != ar[ny][nx]) continue;
					
					Q.push({ny, nx, f.y, f.x});
				}
			}
		}
	}
	
	return false;
}

int main() {
  ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);

	cin >> N >> M;
	for1(0, N) cin >> ar[i];
	
	cout << (bfs() ? "Yes" : "No");
}