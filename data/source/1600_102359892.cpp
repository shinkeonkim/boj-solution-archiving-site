/*
[1600: 말이 되고픈 원숭이](https://www.acmicpc.net/problem/1600)

Tier: Gold 3
Category: graphs, graph_traversal, bfs
*/


#include <bits/stdc++.h>

using namespace std;

#define forn(i, s, e) for(int (i)=s; (i) < e; (i)++)
#define forEach(i, k) for(auto (i) : k)
#define sz(vct) vct.size()
#define all(vct) vct.begin(), vct.end()
#define sortv(vct) sort(vct.begin(), vct.end())
#define uniq(vct) sort(all(vct));vct.erase(unique(all(vct)), vct.end())
#define fi first
#define se second
#define INF (1ll << 60ll)

typedef unsigned long long ull;
typedef long long ll;
typedef ll llint;
typedef unsigned int uint;
typedef unsigned long long int ull;
typedef ull ullint;

typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef pair<double, double> pdd;
typedef pair<double, int> pdi;
typedef pair<string, string> pss;

typedef vector<int> iv1;
typedef vector<iv1> iv2;
typedef vector<ll> llv1;
typedef vector<llv1> llv2;

typedef vector<pii> piiv1;
typedef vector<piiv1> piiv2;
typedef vector<pll> pllv1;
typedef vector<pllv1> pllv2;
typedef vector<pdd> pddv1;
typedef vector<pddv1> pddv2;

const double EPS = 1e-8;
const double PI = acos(-1);

template<typename T>
T sq(T x) { return x * x; }

int sign(ll x) { return x < 0 ? -1 : x > 0 ? 1 : 0; }
int sign(int x) { return x < 0 ? -1 : x > 0 ? 1 : 0; }
int sign(double x) { return abs(x) < EPS ? 0 : x < 0 ? -1 : 1; }

ll K, W, H;
llv2 grid;
ll dp[220][220][33];

ll dy[] = { 0, 0, 1, -1, 1, 1, -1, -1, 2, 2, -2, -2 };
ll dx[] = { 1, -1, 0, 0, 2, -2, 2, -2, 1, -1, 1, -1 };

struct Node {
  ll y, x, cnt, cost;
};

void solve() {
  cin >> K >> W >> H;

  grid = llv2(H, llv1(W, 0));
  
  forn(i, 0, H) {
    forn(j, 0, W) {
      cin >> grid[i][j];

      forn(k, 0, K + 1) {
        dp[i][j][k] = INF;
      }
    }
  }

  queue <Node> Q;

  Q.push({ 0, 0, 0, 0 });

  while(!Q.empty()) {
    Node front = Q.front(); Q.pop();
    auto [y, x, cnt, cost] = front;
    if(dp[y][x][cnt] <= cost) continue;

    dp[y][x][cnt] = cost;

    for(int d = 0; d < 4; d++) {
      ll ny = y + dy[d];
      ll nx = x + dx[d];

      if(ny < 0 || nx < 0 || ny >= H || nx >= W) continue;
      if(grid[ny][nx] == 1) continue;
      if(dp[ny][nx][cnt] <= cost + 1) continue;

      Q.push({ ny, nx, cnt, cost + 1 });
    }

    if(cnt < K) {
      for(int d = 4; d < 12; d++) {
        ll ny = y + dy[d];
        ll nx = x + dx[d];

        if(ny < 0 || nx < 0 || ny >= H || nx >= W) continue;
        if(grid[ny][nx] == 1) continue;
        if(dp[ny][nx][cnt + 1] <= cost + 1) continue;

        Q.push({ ny, nx, cnt + 1, cost + 1 });
      }
    }
  }

  ll ans = INF;

  for(int k = 0; k <= K; k++) {
    ans = min(ans, dp[H - 1][W - 1][k]);
  }

  if(ans == INF) {
    cout << -1;
  } else {
    cout << ans << "\n";
  }
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
  
}
