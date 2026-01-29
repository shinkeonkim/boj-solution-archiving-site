/*
[15899: 트리와 색깔](https://www.acmicpc.net/problem/15899)

Tier: Platinum 2
Category: data_structures, sorting, trees, segtree, offline_queries, euler_tour_technique, merge_sort_tree
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
#define MOD 1000000007

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

ll N, M, C;
llv1 color;
llv1 colorMapping;

struct SegTree {
  int n;
  llv2 elements; // 각 세그트리 노드에 포함되는 트리의 노드 색상들 보관

  SegTree(int n) : n(n) {
    elements.resize(4 * n + 5);
  }

  void init(int left, int right, int idx) {
    if(left == right) {
      elements[idx].push_back(colorMapping[left]);
      return;
    }

    int mid = (left + right) / 2;

    init(left, mid, idx * 2);
    init(mid + 1, right, idx * 2 + 1);

    merge(idx, idx * 2, idx * 2 + 1);
  }

  void merge(int parent, int left, int right) {
    ll li = 0;
    ll ri = 0;
    ll l_size = elements[left].size();
    ll r_size = elements[right].size();

    while (li < l_size && ri < r_size) {
      if(elements[left][li] < elements[right][ri]) {
        elements[parent].push_back(elements[left][li++]);
      } else {
        elements[parent].push_back(elements[right][ri++]);
      }
    }

    while(li < l_size) {
      elements[parent].push_back(elements[left][li++]);
    }

    while(ri < r_size) {
        elements[parent].push_back(elements[right][ri++]);
    }
  }

  ll search(ll idx, ll k) {
    // elements[idx]에서 k보다 작거나 같은 수
    return upper_bound(all(elements[idx]), k) - elements[idx].begin();
  }

  ll query(int left, int right, int k, int idx, int start, int end) {
    if(right < start || end < left) return 0;

    if(left <= start && end <= right) return search(idx, k);

    int mid = (start + end) / 2;

    return query(left, right, k, idx * 2, start, mid) + query(left, right, k, idx * 2 + 1, mid + 1, end);
  }

  ll query(int left, int right, int k) {
    return query(left, right, k, 1, 1, n);
  }
};

ll in[220000];
ll out[220000];
bool chk[220000];
llv1 edges[220000];
ll pv;

void dfs(int node) {
  in[node] = ++pv;
  chk[node] = 1;

  forEach(nxt, edges[node]) {
    if(chk[nxt]) continue;

    dfs(nxt);
  }

  out[node] = pv;
}

void solve() {
  cin >> N >> M >> C;
  color.resize(N + 1);
  colorMapping.resize(N + 1);
  
  forn(i, 1, N + 1) {
    cin >> color[i];
  }

  forn(i, 1, N) {
    ll a, b;
    cin >> a >> b;
    edges[a].push_back(b);
    edges[b].push_back(a);
  }

  dfs(1);

  forn(i, 1, N + 1) {
    colorMapping[in[i]] = color[i];
  }

  SegTree seg(N);
  seg.init(1, N, 1);

  ll ans = 0;

  forn(q, 0, M) {
    ll v, c;
    cin >> v >> c; 
    ans += seg.query(in[v], out[v], c);
    ans %= MOD;
  }

  cout << ans;
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
}
