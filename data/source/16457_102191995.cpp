/*
[16457: 단풍잎 이야기](https://www.acmicpc.net/problem/16457)

Tier: Silver 1
Category: bruteforcing, backtracking
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

ll n, m, k;
iv1 needKeys;

int bitCount(int state) {
  int c;
  for (c = 0; state; c++) state &= state - 1;
  return c;
}

string bin(int state) {
  return bitset<8>(state).to_string();
}

void solve() {
  cin >> n >> m >> k;

  needKeys.resize(m);

  forn(i, 0, m) {
    int stat = 0;
    forn(j, 0, k) {
      ll a; cin >> a;
      stat |= (1 << (a - 1));
    }

    needKeys[i] = stat;
  }

  int ans = 0;

  forn(keyboardStat, 1, 1 << (2 * n)) {
    if(bitCount(keyboardStat) > n) continue;
    int cnt = 0;
    
    forEach(skillStat, needKeys) {
      if((skillStat & keyboardStat) == skillStat) {
        cnt++;
      }
    }
    ans = max(ans, cnt);
  }

  cout << ans;
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
  
}
