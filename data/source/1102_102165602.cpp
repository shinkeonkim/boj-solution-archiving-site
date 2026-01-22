/*
[1102: 발전소](https://www.acmicpc.net/problem/1102)

Tier: Platinum 5
Category: dp, bitmask, dp_bitfield
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

ll N;
ll costs[22][22];
string stats;
ll P;

ll dp[22][70000];

int bit_count(int state) {
  int ret = 0;
  while(state > 0) {
    ret += (state & 1);
    state >>= 1;
  }
  return ret;
}

bool is_on(int state, int pos) {
  return (state & (1 << pos)) != 0;
}

bool is_off(int state, int pos) {
  return (state & (1 << pos)) == 0;
}

void solve() {
  cin >> N;
  forn(i, 0, N) {
    forn(j, 0, N) {
      cin >> costs[i][j];
    }
  }

  fill(&dp[0][0], &dp[21][70000], INF);

  cin >> stats;
  cin >> P;

  int current = 0;

  forn(i, 0, N) {
    current *= 2;
    if(stats[N - i - 1] == 'Y') {
      // 맨 앞의 상태를 LSB로 만들기 위해서 거꾸로 처리
      current += 1;
    }
  }

  dp[0][current] = 0;

  forn(currentTurn, 0, N) {
    forn(stat, 0, 1 << N) {
      if(dp[currentTurn][stat] == INF) continue;

      int pos = 1;
      forn(p, 0, N) {
        if((stat & pos) > 0) { // 이미 켜져있는 경우는 스킵
          pos <<= 1;
          continue;
        }

        ll minCost = INF;

        forn(willOnSwitch, 0, N) {
          if(is_on(stat, willOnSwitch)) minCost = min(minCost, costs[willOnSwitch][p]);
        }

        ll cost = dp[currentTurn][stat] + minCost;
        dp[currentTurn + 1][stat | pos] = min(dp[currentTurn + 1][stat | pos], cost);
        pos <<= 1;
      }
    }
  }

  ll ans = INF;

  forn(i, 0, N + 1) {
    forn(stat, 0, 1 << N) {
      if(bit_count(stat) >= P) {
        ans = min(ans, dp[i][stat]);
      }
    }
  }

  if(ans == INF) {
    cout << -1;
  } else {
    cout << ans;
  }
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
}
