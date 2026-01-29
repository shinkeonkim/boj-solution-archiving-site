/*
[2723: 눌러서 잠금 해제](https://www.acmicpc.net/problem/2723)

Tier: Gold 3
Category: math, dp, combinatorics, bitmask, dp_bitfield
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

#define MX 12

llv1 dp; // i 개의 숫자를 모두 다 사용했을떄의 경우의 수
llv2 dp2; // 집합의 분할
llv2 nCr; // 조합

ll factorial(ll a) {
  if(a <= 1) return 1;
  ll ret = 1;
  forn(i, 2, a + 1) {
    ret *= i;
  }
  return ret;
}

ll partitionSetNumber(ll n, ll k) {
  ll &ret = dp2[n][k];
  if(n == k) return ret = 1;
  if(k == 1) return ret = 1;
  if(k == 2) return ret = (1 << (n - 1)) - 1;

  return ret = partitionSetNumber(n - 1, k - 1) + k * partitionSetNumber(n - 1, k);
}

ll getNCR(ll n, ll r) {
  if(r == 0 || n == r) return 1;
  ll &ret = nCr[n][r];
  if(ret != 0) return ret;
  return ret = getNCR(n - 1, r - 1) + getNCR(n - 1, r);
}

void init() {
  dp.resize(MX);
  dp2.resize(MX, llv1(MX, 0));
  nCr.resize(MX, llv1(MX, 0));

  forn(i, 1, MX) {
    forn(j, 1, i + 1) {
      dp[i] += partitionSetNumber(i, j) * factorial(j);
    }
  }
}

ll f(ll n) {
  ll ret = 0;
  forn(i, 0, n) {
    ret += dp[n - i] * getNCR(n, n - i);
  }

  return ret;
}

void solve() {
  ll N;
  cin >> N;
  cout << f(N) << "\n";
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; cin >> tc;
  init();
  while(tc--) solve();
}