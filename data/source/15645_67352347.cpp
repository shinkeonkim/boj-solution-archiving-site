#include <bits/stdc++.h>

using namespace std;

#define for1(s, e) for(int i = s; i < e; i++)
#define for1j(s, e) for(int j = s; j < e; j++)
#define forEach(k) for(auto i : k)
#define forEachj(k) for(auto j : k)
#define sz(vct) a.size())
#define all(vct) vct.begin(), vct.end()
#define uniq(vct) sort(all(vct));vct.erase(unique(all(vct)), vct.end())
#define fi first
#define se second

typedef unsigned long long ull;
typedef long long ll;
typedef __int128 llll;
typedef unsigned int uint;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef pair<double, double> pdd;
typedef pair<double, int> pdi;
typedef pair<string, string> pss;

const double EPS = 1e-8;
const double PI = acos(-1);

template<typename T>
T sq(T x) { return x * x; }

ll N;
ll ar[110000][3];
ll mn[110000][3];
ll mx[110000][3];

void solve() {
  cin >> N;
  
  for1(0, N) {
    for1j(0, 3) {
      cin >> ar[i][j];
    }
  }
  
  for1(0, 3) {
    mn[0][i] = mx[0][i] = ar[0][i];
  }
  
  for1(1, N) {
    mn[i][0] = ar[i][0] + min(mn[i - 1][0], mn[i - 1][1]);
    mx[i][0] = ar[i][0] + max(mx[i - 1][0], mx[i - 1][1]);

    mn[i][1] = ar[i][1] + min(mn[i - 1][0], min(mn[i - 1][1], mn[i - 1][2]));
    mx[i][1] = ar[i][1] + max(mx[i - 1][0], max(mx[i - 1][1], mx[i - 1][2]));

    mn[i][2] = ar[i][2] + min(mn[i - 1][1], mn[i - 1][2]);
    mx[i][2] = ar[i][2] + max(mx[i - 1][1], mx[i - 1][2]);
  }
  
  ll ans_mn = 1e9;
  ll ans_mx = 0;
  
  for1(0, 3) {
    ans_mx = max(ans_mx, mx[N - 1][i]);
    ans_mn = min(ans_mn, mn[N - 1][i]);
  }
  
  cout << ans_mx << " " << ans_mn;
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
  
}