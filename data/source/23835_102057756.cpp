/*
[23835: 어떤 우유의 배달목록 (Easy)](https://www.acmicpc.net/problem/23835)

Tier: Gold 4
Category: graphs, graph_traversal, trees, dfs
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

ll N, Q;
llv2 edges;
vector <bool> chk;
llv1 cnt;

bool dfs(ll current, ll destination, ll order) {
  if(chk[current]) return false;

  chk[current] = true;

  if(current == destination) {
    cnt[current] += order;
    return true;
  }
  bool ret = false;
  for(auto nxt : edges[current]) {
    if(chk[nxt]) continue;

    ret |= dfs(nxt, destination, order + 1);
  }

  if(ret) {
    cnt[current] += order;
  }

  return ret;
}

void solve() {
  cin >> N;

  cnt.resize(N + 1);
  edges.resize(N + 1);
  for1(1, N) {
    ll a, b;
    cin >> a >> b;

    edges[a].push_back(b);
    edges[b].push_back(a);
  }

  cin >> Q; 
  while(Q--) {
    ll q, a, b;

    cin >> q;

    if(q == 1) {
      cin >> a >> b;
      chk.clear();
      chk.resize(N + 1, false);

      dfs(a, b, 0);

    } else {
      cin >> a;
      cout << cnt[a] << "\n";
    }

  } 
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
  
}
