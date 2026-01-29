/*
[30685: 버터 녹이기](https://www.acmicpc.net/problem/30685)

Tier: Silver 2
Category: implementation, sorting, case_work, parametric_search
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
vector <pll> ar; // 위치, 높이

void solve() {
  cin >> N; ar.resize(N);

  forn(i, 0, N) {
    cin >> ar[i].first >> ar[i].second;
  }

  sortv(ar);

  ll s = 1;
  ll e = 1ll << 40;
  ll ans = 0;

  bool isTotalOver = false;

  while(s <= e) {
    ll mid = (s + e) / 2;

    bool isOver = false;

    for(int i = 1; i < N; i++) {
      pll prev = ar[i - 1];
      pll crt = ar[i];

      ll between = crt.first - prev.first - 1;
      ll meltedMount = min(mid, (prev.second - 1) / 2) + min(mid, (crt.second - 1) / 2);

      if(between < meltedMount) {
        isOver = true;
        isTotalOver = true;
      }
    }

    if(isOver) {
      e = mid - 1;
    } else {
      ans = max(ans, mid);
      s = mid + 1;
    }
  }
  
  if(!isTotalOver) {
    cout << "forever";
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
