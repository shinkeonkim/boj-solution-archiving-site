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

ll N, x, y;

int nim(int x, int y) {
	return (x + y) % 3 + ((x / 3) ^ (y / 3)) * 3;
}

// ll D[3300][3300];
// int dy[] = { 0, -1, -1 };
// int dx[] = { -1, 0, -1 };

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	
	int ans;
	cin >> N;
	cin >> x >> y;
	
	ans = nim(x, y);
	for1(1, N) {
		cin >> x >> y;
		ans = ans ^ nim(x, y);
	}
	
	cout << (ans == 0 ? "cubelover" : "koosaga");
	
	// for(int y = 0; y <= 100; y++) {
	// 	for(int x = 0; x <= 100; x++) {
	// 		vector<bool> chk(100);
			
	// 		for(int x1 = 0; x1 < x; x1++) {
	// 			chk[D[y][x1]] = true;
	// 		}
			
	// 		for(int y1 = 0; y1 < y; y1++) {
	// 			chk[D[y1][x]] = true;
	// 		}
			
	// 		for(int d = 0; d < 3; d++) {
	// 			int ny = y + dy[d];
	// 			int nx = x + dx[d];
				
	// 			if(ny < 0 || nx < 0) continue;
	// 			chk[D[ny][nx]] = true;
	// 		}
						
	// 		for(int k = 0;; k++) {
	// 			if(!chk[k]) {
	// 				D[y][x] = k;
	// 				break;
	// 			}
	// 		}
	// 	}
	// }
	
	// for(int y = 0; y < 50; y++) {
	// 	for(int x = 0; x < 50; x++) {
	// 		cout << D[y][x] << " ";
	// 	}
	// 	cout << "\n";
	// }
	
	
}