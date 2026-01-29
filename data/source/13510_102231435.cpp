/*
[13510: 트리와 쿼리 1](https://www.acmicpc.net/problem/13510)

Tier: Platinum 1
Category: data_structures, trees, segtree, hld
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

#define MAX_V 110000

struct SegTree {
  ll tree[1 << 18];
  int sz = 1 << 17;

  void update(int x, ll v) {
    x |= sz;
    tree[x] = v;

    while(x >>= 1) {
      tree[x] = max(tree[x << 1], tree[x << 1 | 1]);
    }
  }

  ll query(int l, int r) {
    l |= sz; r |= sz;

    ll ret = 0;

    while(l <= r) {
      if(l & 1) ret = max(tree[l++], ret);
      if(~r & 1) ret = max(tree[r--], ret);
      l >>= 1, r >>= 1;
    }

    return ret;
  }
};

struct Edge {
  ll from, to, cost;
};

SegTree seg;
ll sz[MAX_V]; // 노드 i를 루트로 둔 서브트리의 크기
ll dep[MAX_V]; // 노드 i의 깊이
ll par[MAX_V]; // 노드 i의 부모
ll top[MAX_V]; // 노드 i가 속한 체인의 가장 위 부모 노드

ll in[MAX_V]; // DFS ordering, 이를 이용해서 Seg Tree를 사용함.
ll pv;

vector<ll> g[MAX_V];

// 입력 처리용
vector<Edge> inp[MAX_V];
bool chk[MAX_V];
vector<Edge> edges;
int edgeMapping[MAX_V];

void update(int v, ll w) {
  seg.update(in[v], w);
}

ll query(int a, int b) {
  ll ret = 0;

  while(top[a] != top[b]) {
    if(dep[top[a]] > dep[top[b]]) swap(a, b);
    int top_b = top[b];

    ret = max(ret, seg.query(in[top_b], in[b]));
    b = par[top_b];
  }

  if(dep[a] > dep[b]) swap(a, b);

  if(a != b) {
    // 간선에 대한 쿼리라서 해당 경우를 고려해야 함.
    // -> https://www.acmicpc.net/board/view/61839
    ret = max(ret, seg.query(in[a] + 1, in[b]));
  }

  return ret;
}

void dfs(int v = 1) {
  chk[v] = 1;

  for(Edge e : inp[v]) {
    int i = e.to;
    if(chk[i]) continue;
    g[v].push_back(i);
    dfs(i);
  }
}

void dfs1(int v = 1) {
  /*
    sz, dep, par 초기화
  */
  sz[v] = 1;

  for(auto &i : g[v]) {
    dep[i] = dep[v] + 1; par[i] = v;
    dfs1(i);
    sz[v] += sz[i];
    if(sz[i] > sz[g[v][0]]) {
      swap(i, g[v][0]);
    }
  }
}

void dfs2(int v = 1) {
  in[v] = ++pv;

  for(auto i : g[v]) {
    top[i] = (i == g[v][0] ? top[v] : i);
    dfs2(i);
  }
}

void solve() {
  int n, q, e;
  cin >> n;

  for(int i = 0; i < n - 1; i++) {
    int s, e, cost;
    cin >> s >> e >> cost;
    edges.push_back({ s, e, cost });
    inp[s].push_back({ s, e, cost });
    inp[e].push_back({ e, s, cost });
  }

  dfs(); dfs1();

  for(int i = 0; i < edges.size(); i++) {
    Edge edge = edges[i];
    auto [s, e, cost] = edge;
    if(dep[s] > dep[e]) swap(s, e);
    edgeMapping[i + 1] = e;
  }
  
  dfs2();

  // 초기값 업데이트
  for(int i = 0; i < edges.size(); i++) {
    Edge edge = edges[i];
    update(edgeMapping[i + 1], edge.cost);
  }

  cin >> q;

  while(q--) {
    int op, a, b;
    cin >> op >> a >> b;

    if(op == 1) update(edgeMapping[a], b);
    else cout << query(a, b) << "\n";
  }
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
}
