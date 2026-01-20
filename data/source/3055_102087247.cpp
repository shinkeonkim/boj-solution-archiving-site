/*
[3055: 탈출](https://www.acmicpc.net/problem/3055)

Tier: Gold 4
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

ll R, C;
vector<string> grid;

llv2 waterTurn;
llv2 animalTurn;

pll destination;

ll dx[] = {0, 0, 1, -1};
ll dy[] = {1, -1, 0, 0};

struct Node {
  ll y, x, cnt;
};

void solve() {
  cin >> R >> C;

  grid.resize(R);
  waterTurn = llv2(R, llv1(C, INF));
  animalTurn = llv2(R, llv1(C, INF));

  queue <Node> Q;
  queue <Node> AnimalQ;

  for1(0, R) cin >> grid[i];

  for1(0, R) {
    for1j(0, C) {
      if(grid[i][j] == 'D') {
        destination = {i , j};
        continue;
      }

      if(grid[i][j] == '*') {
        waterTurn[i][j] = 0;
        Q.push({ i, j, 0});
      }

      if(grid[i][j] == 'S') {
        animalTurn[i][j] = 0;
        AnimalQ.push({ i, j, 0 });
      }
    }
  }

  while(!Q.empty()) {
    auto [y, x, cnt] = Q.front(); Q.pop();

    for(int d = 0; d < 4; d++) {
      ll ny = y + dy[d];
      ll nx = x + dx[d];

      if(ny < 0 || nx < 0 || ny >= R || nx >= C) continue;

      if(grid[ny][nx] == 'X') {
        continue;
      }

      if(grid[ny][nx] == 'D') {
        continue;
      }

      if(waterTurn[ny][nx] <= cnt + 1) {
        continue;
      }

      waterTurn[ny][nx] = cnt + 1;
      Q.push({ ny, nx, cnt + 1});
    }
  }

  while(!AnimalQ.empty()) {
    auto [y, x, cnt] = AnimalQ.front(); AnimalQ.pop();

    for(int d = 0; d < 4; d++) {
      ll ny = y + dy[d];
      ll nx = x + dx[d];

      if(ny < 0 || nx < 0 || ny >= R || nx >= C) continue;

      if(grid[ny][nx] == 'X') {
        continue;
      }

      if(animalTurn[ny][nx] <= cnt + 1) {
        continue;
      }

      if(waterTurn[ny][nx] <= cnt + 1) {
        continue;
      }

      animalTurn[ny][nx] = cnt + 1;
      AnimalQ.push({ ny, nx, cnt + 1});
    }
  }

  ll dis = animalTurn[destination.first][destination.second];

  if(dis == INF) {
    cout << "KAKTUS";
  } else {
    cout << dis;
  }
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
  
}
