#include <bits/stdc++.h>

#define for1(s,n) for(int i = s; i < n; i++)
#define for1j(s, e) for(int j = s; j < e; j++)

#define foreach(k) for(auto i : k)
#define foreachj(k) for(auto j : k) 
#define pb(a) push_back(a)
#define sz(a) a.size()
#define all(vct) vct.begin(), vct.end()
#define uniq(vct) sort(all(vct));vct.erase(unique(all(vct)), vct.end())
#define fi first
#define se second
#define taxi_dis(a, b) abs(a.fi - b.fi) + abs(a.se - b.se)

using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int uint;

typedef vector <int> iv1;
typedef vector <vector<int> > iv2;

typedef vector <ll> llv1;
typedef vector <vector <ll> > llv2;

typedef vector <ull> ullv1;
typedef vector <vector <ull> > ullv2;

typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef pair<double, double> pdd;
typedef pair<string, string> pss;

void solve() {
    ll n, s, p;

    cin >> n >> s >> p;

    vector <pll> points;

    for1(0, n + 1) {
        pii a;

        cin >> a.fi >> a.se;

        points.push_back(a);
    }

    ll d = 0;

    for1(0, n) {
        d += abs(points[i].fi - points[i + 1].fi) + abs(points[i].se - points[i + 1].se);
    }

    cout << ceil((double)d * s / p) << "\n\n";

}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);

  int tc = 1;

  cin >> tc;

  for(int t = 1; t <= tc; t++) {
      cout << "Data Set " << t <<":\n";
    solve();
  }
}