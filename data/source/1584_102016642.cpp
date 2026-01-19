/*
[1584: 게임](https://www.acmicpc.net/problem/1584)

Tier: Gold 5
Category: graphs, graph_traversal, shortest_path, dijkstra, 0_1_bfs
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

#define DANGER 1
#define DEATH 2

ll N, M;
llv2 grid;
llv2 dp;

ll dy[] = { 0, 0, 1, -1};
ll dx[] = { 1, -1, 0, 0};

struct Node {
  ll y, x, lost_life;
  
  bool operator <(Node other) const {
    return lost_life > other.lost_life;
  }
};

void check(ll x1, ll x2, ll y1, ll y2, ll color) {
  for(int y = min(y1, y2); y <= max(y1, y2); y++) {
    for(int x = min(x1, x2); x <= max(x1, x2); x++) {
      grid[y][x] = max(grid[y][x], color);
    }
  }
}

void solve() {
  cin >> N;
  grid = llv2(501, llv1(501, 0));
  dp = llv2(501, llv1(501, INF)); 

  for1(0, N) {
    ll x1, y1, x2, y2;
    cin >> x1 >> y1 >> x2 >> y2;

    check(x1, x2, y1, y2, DANGER);
  }

  cin >> M;

  for1(0, M) {
    ll x1, y1, x2, y2;
    cin >> x1 >> y1 >> x2 >> y2;

    check(x1, x2, y1, y2, DEATH);
  }

  // for1(0, 501) {
  //   for1j(0, 501) {
  //     cout << grid[i][j] << " ";
  //   }
  //   cout << "\n";
  // }

  priority_queue <Node> Q;

  Q.push({ 0, 0, 0 });

  while(!Q.empty()) {
    Node front = Q.top(); Q.pop();

    auto [y, x, lost_life] = front;

    // cout << y << " " << x << " " << lost_life << "\n";

    if(dp[front.y][front.x] <= lost_life) continue;

    dp[front.y][front.x] = lost_life;

    for(int d = 0; d < 4; d++) {
      ll ny = y + dy[d];
      ll nx = x + dx[d];

      if (ny < 0 || nx < 0 || ny > 500 || nx > 500) continue;
      if(grid[ny][nx] == DEATH) continue;

      ll cost = (grid[ny][nx] == DANGER);
      
      if(dp[ny][nx] <= lost_life + cost) continue;

      Q.push({ ny, nx, lost_life + cost });
    }
  }

  cout << (dp[500][500] == INF ? -1 : dp[500][500]);
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
  
}
