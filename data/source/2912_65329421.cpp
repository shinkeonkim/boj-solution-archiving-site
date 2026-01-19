#include <bits/stdc++.h>

using namespace std;

#define for1(s, e) for(int i = s; i < e; i++)
#define for1j(s, e) for(int j = s; j < e; j++)
#define forEach(k) for(auto i : k)
#define forEachj(k) for(auto j : k)
#define sz(vct) a.size())
#define all(vct) vct.begin(), vct.end()
#define uniq(vct) sort(all(vct)), vct.erase(unique(all(vct)), vct.end())
#define fi first
#define se second
#define _rand mt19937((unsigned)chrono::steady_clock::now().time_since_epoch().count());

typedef unsigned long long ull;
typedef long long ll;
typedef __int128 llll;
typedef unsigned int uint;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef pair<double, double> pdd;
typedef pair<double, int> pdi;
typedef pair<string, string> pss;
typedef double radian_angle;

mt19937 rd = _rand;

void solve() {
  int n, c, m, s, e;
  vector<int> v;
  vector<int> pos[11000];

  cin >> n >> c; v.resize(n + 1);

  for1(1, n + 1) {
    cin >> v[i];

    if(pos[v[i]].empty()) pos[v[i]].emplace_back(-1);
    pos[v[i]].emplace_back(i);
  }

  cin >> m;

  while(m--) {
    cin >> s >> e;
    int ans = -1;

    uniform_int_distribution<int> rnd(s, e);

    for1(0, 100) {
      int idx = rnd(rd);
      int val = v[idx];

      int cnt = upper_bound(pos[val].begin(), pos[val].end(), e) - lower_bound(pos[val].begin(), pos[val].end(), s);
      if(cnt * 2 > (e - s + 1)) {
        ans = val;
      }
    }

    if(ans < 0) cout << "no\n";
    else cout << "yes " << ans << "\n";
  }
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
}