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

int N, M, ans;
string a[550];
bool visited[550][550];
bool possible[550][550]; 

bool dfs(int y, int x) {
	if(y < 0 || x < 0 || y >= N || x >= M) return true;
	if(visited[y][x]) return possible[y][x];
	
	visited[y][x] = true;
	
	int ny = y;
	int nx = x;
	
	switch(a[y][x]) {
		case 'U':
			ny -= 1;
			break;
		case 'D':
			ny += 1;
			break;
		case 'L':
			nx -= 1;
			break;
		case 'R':
			nx += 1;
			break;
	}
	
	return possible[y][x] = dfs(ny, nx);
}

int main() {
  ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	
	cin >> N >> M;
	
	for1(0, N) cin >> a[i];
	
	for1(0, N) {
		for1j(0, M) {
			if(visited[i][j]) continue;
			
		  dfs(i, j);
		}
	}
	
	for1(0, N) {
		for1j(0, M) {
			if(possible[i][j]) ans++;
		}
	}
	
	cout << ans;
}