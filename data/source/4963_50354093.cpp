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

int W, H, ans;
int ar[55][55];
bool check[55][55];
int dx[] = { 0, 0, 1, -1, 1, 1, -1, -1 };
int dy[] = { 1, -1, 0, 0, 1, -1, 1, -1 };

void dfs(int y, int x) {
  check[y][x] = true;

  for(int d = 0; d < 8; d++) {
    int ny = y + dy[d];
    int nx = x + dx[d];

    if(ny < 0 || nx < 0 || ny >= H || nx >= W) continue;

    if(!check[ny][nx] && ar[ny][nx] == 1) {
      dfs(ny, nx);
    }
  }
}

int main() {
  ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);

  while(1) {
    ans = 0;
    cin >> W >> H;

    if(W == 0 && H == 0) break;

    for(int y = 0; y < 55; y++) {
      for(int x = 0; x < 55; x++) {
        check[y][x] = false;
        ar[y][x] = 0;
      }
    }

    for(int y = 0; y < H; y++) {
      for(int x = 0; x < W; x++) {
        cin >> ar[y][x];
      }
    }

    for(int y = 0; y < H; y++) {
      for(int x = 0; x < W; x++) {
        if(!check[y][x] && ar[y][x] == 1) {
          dfs(y, x);
          ans++;
        }
      }
    }

    cout << ans << "\n";
  }
}