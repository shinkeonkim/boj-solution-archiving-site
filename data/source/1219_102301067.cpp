/*
[1219: 오민식의 고민](https://www.acmicpc.net/problem/1219)

Tier: Platinum 5
Category: graphs, graph_traversal, shortest_path, bellman_ford
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

struct BellmanFord {
  struct BellmanEdge {
    ll to, cost;

    BellmanEdge(ll to, ll cost) : to(to), cost(cost) {}
  };

  ll N;
  vector<vector <BellmanEdge> > adj;
  llv1 D;
  vector<vector <BellmanEdge>> rev; // 역방향
  vector<bool> chk; // 도착점까지 가는 길에 사이클로 영향을 주는 노드인가?

  BellmanFord(ll N) : N(N) {
    adj.resize(N + 1);
    rev.resize(N + 1);
    chk.resize(N + 1, false);
  }

  void addEdge(ll s, ll e, ll cost) {
    adj[s].push_back(BellmanEdge(e, cost));
    rev[e].push_back(BellmanEdge(s, cost));
  }

  void bfs_reverse(ll start) {
    queue <ll> Q;

    Q.push(start);

    while(!Q.empty()) {
      ll front = Q.front(); Q.pop();

      if(chk[front]) continue;

      chk[front] = true;

      for(auto nxt : rev[front]) {
        if(chk[nxt.to]) continue;
        
        Q.push(nxt.to);
      }
    }
  }

  bool run(ll start_point, ll initial_distance, ll end_point) {
    D.resize(N + 1, INF);
    D[start_point] = initial_distance;
    bfs_reverse(end_point);
  
    bool isCycle = false;

    forn(i, 1, N + 1) {
      forn(j, 1, N + 1) {
        for(int k=0; k < sz(adj[j]); k++) {
          BellmanEdge p = adj[j][k];
          int end = p.to;
          ll dist = D[j] + p.cost;

          if (D[j] != INF && D[end] > dist) {
            D[end] = dist;
            if (i == N && chk[end]) isCycle = true;
          }
        }
      }
    }
    return isCycle;
  }
};

struct st {
  ll s, e, cost;
};

ll N, source, destination, M;
llv1 gain;
vector <st> inp;

void solve() {
  cin >> N >> source >> destination >> M;
  inp.resize(M);
  gain.resize(N + 1);
  source++;
  destination++;

  forn(i, 0, M) {
    cin >> inp[i].s >> inp[i].e >> inp[i].cost;
    inp[i].s++;
    inp[i].e++;
  }

  forn(i, 1, N + 1) {
    cin >> gain[i];
  }

  BellmanFord bf(N); // 1-index struct

  forn(i, 0, M) {
    bf.addEdge(inp[i].s, inp[i].e, inp[i].cost - gain[inp[i].e]);
  }

  bool isCycle = bf.run(source, -gain[source], destination);

  if(bf.D[destination] >= INF) {
    cout << "gg";
    return;
  }

  if(isCycle) {
    cout << "Gee";
    return;
  }

  cout << -bf.D[destination];
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
}
