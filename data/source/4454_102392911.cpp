/*
[4454: 상근이의 여자친구](https://www.acmicpc.net/problem/4454)

Tier: Silver 1
Category: binary_search, parametric_search
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
#define MX 100000000

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

double a, b, c, d, m, t;

double oil_per_hour(double v) {
  return pow(v, 4) * a + pow(v, 3) * b + pow(v, 2) * c + d * v;
}

void solve() {
  // t: 기름의 양, m : 거리  
  cout << fixed << setprecision(2);

  while(cin >> a >> b >> c >> d >> m >> t) {
    double ans = 0;
    double s = 0;
    double e = MX;
  
    while(s <= e) {
      double mid = (s + e) / 2; // 속도

      double need_time = m / mid;
      double need_oil = oil_per_hour(mid) * need_time;

      if (need_oil >= t) {
        e = mid - EPS;
      } else {
        ans = max(ans, mid);
        s = mid + EPS;
      }
    }

    ans = floor(ans * 100) / 100.0;

    cout << ans << "\n";
  }
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
  
}
