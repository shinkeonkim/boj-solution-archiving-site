/*
[17407: 괄호 문자열과 쿼리](https://www.acmicpc.net/problem/17407)

Tier: Platinum 3 
Category: data_structures, lazyprop, segtree
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

int tree[440000]; // prefix sum의 min value
int lazy[440000];

int ar[110000];
int state[110000];

int n;

void propagate(int node, int s, int e) {
  if(lazy[node] == 0) return;
  tree[node] += lazy[node];
  if(s != e) {
    lazy[node * 2] += lazy[node];
    lazy[node * 2 + 1] += lazy[node];
  }
  lazy[node] = 0;
}

void build(int node, int start, int end) {
  if(start == end) {
    tree[node] = ar[start];
    return;
  }

  int mid = (start + end) / 2;
  build(node * 2, start, mid);
  build(node * 2 + 1, mid + 1, end);
  tree[node] = min(tree[node * 2], tree[node * 2 + 1]);
}

void update(int x, int node, int left, int right, int start, int end) {
  propagate(node, start, end);
  if(right < start || end < left) return;

  if(left <= start && end <= right) {
    lazy[node] += x;
    propagate(node, start, end);
    return;
  }

  int mid = (start + end) / 2;
  update(x, node * 2, left, right, start, mid);
  update(x, node * 2 + 1, left, right, mid + 1, end);
  tree[node] = min(tree[node * 2], tree[node * 2 + 1]);
}

int query(int node, int left, int right, int start, int end) {
  propagate(node, start, end);
  if(right < start || end < left) return INF;
  if(left <= start && end <= right) return tree[node];

  int mid = (start + end) / 2;
  return min(query(node * 2, left, right, start, mid), query(node * 2 + 1, left, right, mid + 1, end));
}

void update(int x, int left, int right) {
  update(x, 1, left, right, 1, n);
}

int query(int left, int right) {
  return query(1, left, right, 1, n);
}

void solve() {
  int ans = 0;

  string s; cin >> s;
  int crt = 0;
  n = s.size();

  for1(0, n) {
    if(s[i] == '(') {
      crt++;
      state[i + 1] = 1;
    }
    else {
      crt --;
      state[i + 1] = -1;
    }
    ar[i + 1] = crt;
  }

  for1(0, 440000) tree[i] = INF;
  build(1, 1, n);

  int q; cin >> q;
  while(q--) {
    int idx;

    cin >> idx;

    int nxt = -state[idx];
    int diff = nxt - state[idx];
    state[idx] = nxt;
    update(diff, 1, idx, n, 1, n);

    if(query(1, n) >= 0 && query(n, n) == 0) ans++;

    // for(int i = 1; i <= n; i++) {
    //   cout << query(i, i) << " ";
    // }

    // cout << query(1, n) << " " << query(n, n) << "\n";
  }

  cout << ans << "\n";
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
  
}