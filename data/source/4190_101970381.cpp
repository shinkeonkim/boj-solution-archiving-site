/*
[4190: Exact Change](https://www.acmicpc.net/problem/4190)

Tier: Gold 5
Category: dp, knapsack
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

#define MX 40000

llv1 D;

ll DP(llv1 &coin, ll money) {
  D.clear();
  D.resize(2 * MX + 1, INF);
  D[0] = 0;

  for (int i = 0; i < coin.size(); i++) {
    for (int j = money; j >= coin[i]; j--) {
      D[j] = min(D[j], D[j - coin[i]] + 1);
    }
  }
  return D[money];
}

void solve() {
  ll money;
  ll N;
  llv1 coins;

  cin >> money >> N;
  coins.resize(N);

  for1(0, N) {
    cin >> coins[i];
  }

  sort(coins.begin(), coins.end(), greater<ll>());

  DP(coins, MX);
  
  for(int i = money; i <= MX; i++) {
    if(D[i] != INF) {
      cout << i << " " << D[i] << "\n";
      return;
    }
  }
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; cin >> tc;
  while(tc--) solve();
  
}
