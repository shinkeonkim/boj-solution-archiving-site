/*
[4179: 불!](https://www.acmicpc.net/problem/4179)

Tier: Gold 3
Category: graphs, graph_traversal, bfs, grid_graph
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

#define WALL '#'

ll N, M;
vector<string> grid;
llv2 fireTurn;
llv2 personTurn;

ll dy[] = { 0, 0, 1, -1};
ll dx[] = { 1, -1, 0, 0};

struct Node {
  ll y, x, turn;
};

void solve() {
  cin >> N >> M;
  grid.resize(N);
  fireTurn = llv2(N, llv1(M, INF));
  personTurn = llv2(N, llv1(M, INF));

  for1(0, N) {
    cin >> grid[i];
  }

  queue <Node> q;
  queue <Node> fireQ;

  for1(0, N) {
    for1j(0, M) {
      if(grid[i][j] == 'J') {
        q.push({i, j, 0});
        personTurn[i][j] = 0;
      }

      if(grid[i][j] == 'F') {
        fireQ.push({i, j, 0});
        fireTurn[i][j] = 0;
      }
    }
  }

  while(!fireQ.empty()) {
    Node front = fireQ.front(); fireQ.pop();

    auto [y, x, turn] = front;

    for(int d = 0; d < 4; d++) {
      ll ny = y + dy[d];
      ll nx = x + dx[d];

      if(ny < 0 || nx < 0 || ny >= N || nx >= M) continue;
      if(grid[ny][nx] == WALL) continue;

      if(fireTurn[ny][nx] <= turn + 1) continue;

      fireTurn[ny][nx] = turn + 1;
      fireQ.push({ ny, nx, turn + 1});
    }
  }

  ll ans = INF;

  while(!q.empty()) {
    Node front = q.front(); q.pop();

    auto [y, x, turn] = front;

    for(int d = 0; d < 4; d++) {
      ll ny = y + dy[d];
      ll nx = x + dx[d];

      if(ny < 0 || nx < 0 || ny >= N || nx >= M) {
        ans = min(ans, turn + 1);
        continue;
      }
      if(grid[ny][nx] == WALL) continue;

      if(personTurn[ny][nx] <= turn + 1) continue;
      if(fireTurn[ny][nx] <= turn + 1) continue;

      personTurn[ny][nx] = turn + 1;
      q.push({ ny, nx, turn + 1});
    }
  }

  if(ans == INF) {
    cout << "IMPOSSIBLE";
  } else {
    cout << ans;
  }
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
}
