/*
[5547: 일루미네이션](https://www.acmicpc.net/problem/5547)

Tier: Gold 4
Category: graphs, graph_traversal, bfs, dfs
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

ll W, H;
ll ar[110][110];
bool isVisited[110][110]; 
ll ans;

ll directionsCount = 6;
ll dx[][6] = {
  {1, 0, -1, -1, -1, 0 },
  {1, 1, 0, -1, 0, 1},
};
ll dy[2][6] = {
  {0, 1, 1, 0, -1, -1 },
  {0, 1, 1, 0, -1, -1 }
};

void dfs(int y, int x) {
  if(ar[y][x] == 1) return;
  if(isVisited[y][x]) return;

  isVisited[y][x] = true;

  for(int d = 0; d < directionsCount; d++) {
    ll ny = y + dy[y % 2][d];
    ll nx = x + dx[y % 2][d];

    if(ny < 0 || nx < 0 || ny > H + 1|| nx > W + 1) continue;
    if(isVisited[ny][nx]) continue;
    
    if(ar[ny][nx] == 1) {
      ans += 1;
      // cout << y << " " << x << " | " << ny << " " << nx << "\n";
      continue;
    }
    
    dfs(ny, nx);
  }
}

void solve() {
  cin >> W >> H;

  for1(1, H + 1) {
    for1j(1, W + 1) {
      cin >> ar[i][j];
    }
  }

  dfs(0, 0);

  cout << ans;
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
  
}
