/*
[2820: 자동차 공장](https://www.acmicpc.net/problem/2820)

Tier: Platinum 3
Category: data_structures, trees, segtree, lazyprop, euler_tour_technique
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

struct SegTreeWithLazyProp {
  int n;
  vector<ll> tree;
  vector<ll> lazy;

  SegTreeWithLazyProp(int n) : n(n) {
    tree.resize(4 * n + 5, 0);
    lazy.resize(4 * n + 5, 0);
  }

  void _update_prop(int idx, int start, int end) {
    if(lazy[idx] == 0) return;

    tree[idx] += (end - start + 1) * lazy[idx];
    
    if(start != end) {
      lazy[idx * 2] += lazy[idx];
      lazy[idx * 2 + 1] += lazy[idx];
    }

    lazy[idx] = 0;
  }

  void __update(int left, int right, int idx, ll val, int start, int end) {
    _update_prop(idx, start, end);

    if (end < left || start > right) return;

    if(left <= start && end <= right) {
      tree[idx] += (end - start + 1) * val;

      if(start != end) {
        lazy[idx * 2] += val;
        lazy[idx * 2 + 1] += val;
      }

      return;
    }

    int mid = (start + end) / 2;
    __update(left, right, idx * 2, val, start, mid);
    __update(left, right, idx * 2 + 1, val, mid + 1, end);

    tree[idx] = tree[idx * 2] + tree[idx * 2 + 1];
  }

  ll __query(int left, int right, int idx, int start, int end) {
    _update_prop(idx, start, end);

    if (right < start || end < left) return 0;
    if(left <= start && end <= right) return tree[idx];

    int mid = (start + end) / 2;

    return __query(left, right, idx * 2, start, mid) + __query(left, right, idx * 2 + 1, mid + 1, end);
  }

  void update(int Q, ll val) {
    __update(Q, Q, 1, val, 1, n);
  }

  void update_range(int left, int right, ll val) {
    __update(left, right, 1, val, 1, n);
  }

  ll query(int left, int right) {
    return __query(left, right, 1, 1, n);
  }
};

int N, M;
llv1 salaries;
llv1 parent;
llv2 children;
iv1 in;
iv1 out;
int pv;

void dfs(int v = 1) {
  in[v] = ++pv;

  forEach(child, children[v]) {
    dfs(child);
  }

  out[v] = pv;
}

void solve() {
  cin >> N >> M;
  salaries.resize(N + 1);
  parent.resize(N + 1);
  children.resize(N + 1);
  in.resize(N + 1);
  out.resize(N + 1);

  cin >> salaries[1];
  parent[1] = 1;

  forn(i, 2, N + 1) {
    ll a, p;
    cin >> a >> p;

    parent[i] = p;
    salaries[i] = a;
    children[p].push_back(i);
  }

  dfs();

  SegTreeWithLazyProp tree(N + 1);

  forn(i, 1, N + 1) {
    tree.update(in[i], salaries[i]);
  }

  forn(i, 0, M) {
    char q;
    ll a, b;

    cin >> q;

    if(q == 'p') {
      // 자신의 모든 부하의 월급 증가 (자신 제외)
      cin >> a >> b;
      tree.update_range(in[a] + 1, out[a], b);
    } else {
      // 자신의 월급 조회
      cin >> a;
      cout << tree.query(in[a], in[a]) << "\n";
    }
  }
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
}
