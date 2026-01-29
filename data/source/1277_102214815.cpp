/*
[1277: 발전소 설치](https://www.acmicpc.net/problem/1277)

Tier: Gold 4
Category: graphs, shortest_path, dijkstra
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
#define INF 987654321

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

struct PowerStation {
  double y, x;

  double getDistance(PowerStation o) {
    return sqrt((y - o.y) * (y - o.y) + (x - o.x) * (x - o.x)) * 1000;
  }
};

struct Node {
  int to;
  double cost;

  bool operator<(Node o) const {
    return cost > o.cost;
  }
};

PowerStation powerStations[1100];
double weights[1100][1100];
double distances[1100];

void solve() {
  int N, W; // N: 발전소의 수, W : 남아있는 전선의 수
  double M;

  fill(&weights[0][0], &weights[1100][1100], INF);
  fill(&distances[0], &distances[1100], INF);

  cin >> N >> W >> M;

  M *= 1000;

  forn(i, 1, N + 1) {
    cin >> powerStations[i].y >> powerStations[i].x;
  }

  for(int i = 1; i <= N; i++) {
    for(int j = i + 1; j <= N; j++) {
      double dis = powerStations[i].getDistance(powerStations[j]);
      
      if(dis > M) dis = INF;
      weights[i][j] = weights[j][i] = dis;
    }
  }

  forn(i, 0, W) {
    int a, b;
    cin >> a >> b;

    weights[a][b] = 0;
    weights[b][a] = 0;
  }

  priority_queue<Node, vector<Node>> pq;

  pq.push({ 1, 0 });

  while(!pq.empty()) {
    Node top = pq.top(); pq.pop();
    auto [current, cost] = top;

    if(distances[current] <= cost) continue;
    distances[current] = cost;

    for(int nxt = 1; nxt <= N; nxt++) {
      if(distances[nxt] <= cost + weights[current][nxt]) continue;

      pq.push({ nxt, cost + weights[current][nxt]});
    }
  }
  cout << (int)distances[N];
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
}
