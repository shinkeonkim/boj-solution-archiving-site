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

ll D[110000][3];
ll N, ans;
ll ar[110000];

void solve() {
  cin >> N;
  for1(0, N) cin >> ar[i];
  
  if(N == 1) {
    cout << ar[0];
    return;
  }
  
  D[0][0] = ar[0];
  D[1][0] = ar[1];
  D[1][1] = ar[0] + ar[1] / 2;
  
  for1(2, N) {
    ll d = i >= 3 ? max(D[i - 3][0], D[i -3][1]) : 0;
    D[i][0] = max(d, max(D[i - 2][0], D[i - 2][1])) + ar[i];
    D[i][1] = D[i - 1][0] + ar[i] / 2;
  }
  
  for1(0, N) {
    for1j(0, 2) {
      ans = max(ans, D[i][j]);
    }
  }
  cout << ans;
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
}