/*
[18437: 회사 문화 5](https://www.acmicpc.net/problem/18437)

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
  // -1이면 끄고, 1이면 킨다.

  int n;
  vector<ll> tree;
  vector<ll> lazy;

  SegTreeWithLazyProp(int n) : n(n) {
    tree.resize(4 * n + 5, 0);
    lazy.resize(4 * n + 5, 0);
  }

  void _update_prop(int idx, int start, int end) {
    if(lazy[idx] == 0) return;
    
    if(lazy[idx] == -1) {
      tree[idx] = 0;
    } else {
      tree[idx] = (end - start + 1);
    }
    
    if(start != end) {
      lazy[idx * 2] = lazy[idx];
      lazy[idx * 2 + 1] = lazy[idx];
    }

    lazy[idx] = 0;
  }

  void __update(int left, int right, int idx, ll val, int start, int end) {
    _update_prop(idx, start, end);

    if (end < left || start > right) return;
    if(left <= start && end <= right) {
      if(val == 1) {
        tree[idx] = (end - start + 1);
      } else if(val == -1) {
        tree[idx] = 0;
      }

      if(start != end) {
        lazy[idx * 2] = val;
        lazy[idx * 2 + 1] = val;
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
    if(left <= start && end <= right) {
      return tree[idx];
    }

    int mid = (start + end) / 2;

    return __query(left, right, idx * 2, start, mid) + __query(left, right, idx * 2 + 1, mid + 1, end);
  }

  void update(int Q, ll val) {
    __update(Q, Q, 1, val, 1, n);
  }

  void update_range(int left, int right, ll val) {
    if(left > right) return;
    __update(left, right, 1, val, 1, n);
  }

  ll query(int left, int right) {
    if(left > right) return 0;

    return __query(left, right, 1, 1, n);
  }
};

ll N, M;
llv2 children;
ll in[110000];
ll out[110000];
ll pv;

void dfs(int node) {
  in[node] = ++pv;

  forEach(nxt, children[node]) {
    dfs(nxt);
  }

  out[node] = pv;
}

void solve() {
  cin >> N;
  children.resize(N + 1);

  forn(i, 1, N + 1) {
    ll parent;
    cin >> parent;

    if(i == 1) continue;

    children[parent].push_back(i);
  }

  dfs(1);

  SegTreeWithLazyProp seg(N + 1);

  cin >> M;

  seg.update_range(1, N, 1);

  forn(i, 0, M) {
    ll op, a;

    cin >> op >> a;

    switch (op) {
    case 1:
      seg.update_range(in[a] + 1, out[a], 1);
      // 모두 켠다.
      break;
    case 2:
      seg.update_range(in[a] + 1, out[a], -1);
      // 모두 끈다.
      break;
    case 3:
      cout << seg.query(in[a] + 1, out[a]) << "\n";
      // 아래 모두 누적합
      break;
    }
  }
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
}
