/*
[14288: 회사 문화 4](https://www.acmicpc.net/problem/14288)

Tier: Platinum 3
Category: data_structures, trees, segtree, lazyprop, euler_tour_technique, difference_array
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

struct SegTree {
  ll n;
  llv1 tree;
  llv1 lazy;

  SegTree(ll n) {
    this->n = n;
    tree.resize(4 * n + 5);
    lazy.resize(4 * n + 5);
  }

  void propagate(int idx, int start, int end) {
    if(lazy[idx] == 0) return;
    
    tree[idx] += (end - start + 1) * lazy[idx];

    if(start != end) {
      lazy[idx * 2] += lazy[idx];
      lazy[idx * 2 + 1] += lazy[idx];
    }

    lazy[idx] = 0;
  }

  void update(int left, int right, int value, int idx, int start, int end) {
    propagate(idx, start, end);
    // 실제 업데이트 구간 left, right
    if(end < left || right < start) return;

    if(left <= start && end <= right) {
      tree[idx] += (end - start + 1) * value; 

      if(start != end) {
        lazy[idx * 2] += value;
        lazy[idx * 2 + 1] += value;
      }

      return;
    }

    int mid = (start + end) / 2;

    update(left, right, value, idx * 2, start, mid);
    update(left, right, value, idx * 2 + 1, mid + 1, end);

    tree[idx] = tree[idx * 2] + tree[idx * 2 + 1]; 
  }

  ll query(int left, int right, int idx, int start, int end) {
    propagate(idx, start, end);
  
    if(end < left || right < start) return 0;

    if(left <= start && end <= right) {
      return tree[idx];
    }
    
    int mid = (start + end) / 2;

    return query(left, right, idx * 2 , start, mid) + query(left, right, idx * 2 + 1, mid + 1, end);
  }

  void update(int left, int right, int value) {
    update(left, right, value, 1, 1, n);
  }

  ll query(int left, int right) {
    return query(left, right, 1, 1, n);
  }

};


ll n, m, root;
// 1-index
llv1 parent;
llv2 children;
llv1 in;
llv1 out;
ll current_direction = 0;

ll pv = 0;

void dfs(ll current) {
  in[current] = ++pv;

  forEach(child, children[current]) {
    dfs(child);
  }

  out[current] = pv;
}

void solve() {
  cin >> n >> m; // n : 직원 수, m : 쿼리 수
  
  parent.resize(n + 1);
  children.resize(n + 1);
  in.resize(n + 1);
  out.resize(n + 1);
  
  SegTree seg0(n); // 아래 방향으로 전파 -> 구간 업데이트로 처리
  SegTree seg1(n); // 위 방향으로 전파해야 하는-> 실질적으로 쿼리때 서브트리를 모두 조회하는 방식으로 처리

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

  forn(i, 1, m + 1) {
    int operation, a, b;

    cin >> operation;

    if(operation == 3) {
      current_direction = 1 - current_direction;
      continue;
    }

    if(operation == 1) {
      cin >> a >> b;

      if(current_direction == 0) {
        seg0.update(in[a], out[a], b);
      } else {
        seg1.update(in[a], in[a], b);
      }
      
      continue;
    }

    cin >> a;
    // cout << seg0.query(in[a], in[a]) << " " << seg1.query(in[a], out[a]) << "\n";
    cout << seg0.query(in[a], in[a]) + seg1.query(in[a], out[a]) << "\n";
  }
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
}
