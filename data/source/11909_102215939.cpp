/*
[11909: 배열 탈출](https://www.acmicpc.net/problem/11909)

Tier: Gold 5
Category: dp, graphs, shortest_path, dijkstra
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


struct Node {
  ll y, x, cost;

  bool operator<(Node o) const {
    return cost > o.cost;
  }
};

ll N;
ll grid[2300][2300];
ll dis[2300][2300];

ll dx[] = {0, 1};
ll dy[] = {1, 0};

void solve() {
  cin >> N;

  forn(i, 0, N) {
    forn(j, 0, N) {
      cin >> grid[i][j];
      dis[i][j] = INF;
    }
  }

  priority_queue <Node, vector<Node>> pq;

  pq.push({ 0, 0, 0 });

  while(!pq.empty()) {
    auto [y, x, cost] = pq.top(); pq.pop();

    if(dis[y][x] <= cost) continue;

    dis[y][x] = cost;

    for(int d = 0; d < 2; d++) {
      int ny = y + dy[d];
      int nx = x + dx[d];

      if(ny < 0 || nx < 0 || ny >= N || nx >= N) continue;

      ll diff = max(0ll, grid[ny][nx] - grid[y][x] + 1);

      if(dis[ny][nx] <= cost + diff) continue;

      pq.push({ ny, nx, cost + diff });
    }
  }

  cout << dis[N - 1][N - 1];
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
  
}
