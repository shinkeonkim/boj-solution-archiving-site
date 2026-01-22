/*
[5993: Invasion of the Milkweed](https://www.acmicpc.net/problem/5993)

Tier: Silver 2
Category: bfs, graphs, graph_traversal
*/


#include <bits/stdc++.h>

using namespace std;

#define for1(s, e) for(int i = s; i < e; i++)
#define for1j(s, e) for(int j = s; j < e; j++)
#define forEach(k) for(auto i : k)
#define forEachj(k) for(auto j : k)
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

ll N, M;
pll start;
vector<string> grid;
llv2 dp;

ll dy[] = {0, 0, 1, -1, 1, 1, -1, -1};
ll dx[] = {1, -1, 0, 0, 1, -1, 1, -1};

void solve() {
  cin >> M >> N >> start.second >> start.first;
  start.first--;
  start.second--;
  grid.resize(N);
  dp = llv2(N, llv1(M, INF));

  for(int i = N - 1; i >= 0; i--) {
    cin >> grid[i];
  }

  queue <pll> Q;

  ll ans = 0;

  dp[start.first][start.second] = 0;
  Q.push(start);

  while(!Q.empty()) {
    pll front = Q.front(); Q.pop();

    auto [y, x] = front;

    for(int d = 0; d < 8; d++) {
      ll ny = y + dy[d];
      ll nx = x + dx[d];

      if(ny < 0 || nx < 0 || ny >= N || nx >= M) continue;
      if(grid[ny][nx] == '*') continue;
      if(dp[ny][nx] <= dp[y][x] + 1) continue;

      dp[ny][nx] = dp[y][x] + 1;
      Q.push({ ny, nx });
    }
  }

  for1(0, N) {
    for1j(0, M) {
      if(grid[i][j] == '.') {
        ans = max(ans, dp[i][j]);
      }
    }
  }

  cout << ans;
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
  
}
