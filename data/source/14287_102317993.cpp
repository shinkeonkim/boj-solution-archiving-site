/*
[14287: 회사 문화 3](https://www.acmicpc.net/problem/14287)

Tier: Platinum 3
Category: data_structures, trees, segtree, euler_tour_technique
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

ll n, m, root;
// 1-index
llv1 parent;
llv2 children;
llv1 in;
llv1 out;

ll pv = 0;

struct SegTree {
  ll tree[1 << 20];
  int sz = 1 << 19;

  void update(int idx, int v) {
    idx |= sz;
    tree[idx] += v;

    while(idx >>= 1) {
      tree[idx] = tree[idx << 1] + tree[idx << 1 | 1];
    }
  }

  ll query(int left, int right) {
    left |= sz;
    right |= sz;

    ll ret = 0;

    while(left <= right) {
      if(left&1) ret += tree[left++];
      if(~right&1) ret += tree[right--];
      left >>= 1;
      right >>= 1;
    }

    return ret;
  }
};

void dfs(ll current) {
  in[current] = ++pv;

  forEach(child, children[current]) {
    dfs(child);
  }

  out[current] = pv;
}

SegTree seg;

void solve() {
  cin >> n >> m; // n : 직원 수, m : 쿼리 수
  
  parent.resize(n + 1);
  children.resize(n + 1);
  in.resize(n + 1);
  out.resize(n + 1);

  forn(i, 1, n + 1) {
    cin >> parent[i];

    if(parent[i] == -1) {
      root = i;
    } else {
      children[parent[i]].push_back(i);
    }
  }

  assert(root == 1);
  
  dfs(root);

  forn(i, 0, m) {
    int operation, a, b;

    cin >> operation;

    if(operation == 1) {
      // 칭찬을 받는다. 이때
      cin >> a >> b;
      
      seg.update(in[a], b);
    }

    if(operation == 2) {
      // 칭찬을 받은 정도를 출력
      cin >> a;
      cout << seg.query(in[a], out[a]) << "\n";
    }
  }
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
  
}
