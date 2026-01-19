/*
[1516: 게임 개발](https://www.acmicpc.net/problem/1516)

Tier: Gold 3 
Category: dp, graphs, dag, topological_sorting
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

ll n;
ll cost[550];
ll dp[550];
llv1 pre_nodes[550];

ll dfs(ll node) {
  if(dp[node] != 0) return dp[node];

  ll cost_sum = cost[node];

  ll child = 0;
  for(auto pre_node : pre_nodes[node]) {
    child = max(child, dfs(pre_node));
  }

  return dp[node] = cost_sum + child;
}

void solve() {
  cin >> n;

  for1(0, n) {
    cin >> cost[i];

    while(1) {
      int x; cin >> x;
      if (x == -1) break;
      pre_nodes[i].push_back(x - 1);
    }
  }

  for1(0, n) {
    if(dp[i] != 0) continue;

    dp[i] = dfs(i);
  }

  for1(0, n) {
    cout << dp[i] << '\n';
  }
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
  
}
