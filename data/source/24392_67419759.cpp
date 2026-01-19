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
const ll MOD = 1e9+7;

template<typename T>
T sq(T x) { return x * x; }

int ar[1100][1100];
int D[1100][1100];
int N, M;

void solve() {
  cin >> N >> M;
  for(int i = N - 1; i >= 0; i--) {
    for1j(0, M) {
      cin >> ar[i][j];
    }
  }
  
  for1(0, M) {
    D[0][i] = ar[0][i];
  }
  
  for1(1, N) {
    for1j(0, M) {
      if(ar[i][j] == 0) {
        continue;
      }
      for(int d = -1; d <= 1; d++) {
        if(j + d < 0 || j + d >=M) continue;

        D[i][j] += D[i - 1][j + d];
        D[i][j] %= MOD;
      }
    }
  }
  
  ll ans = 0;
  for1(0, M) {
    ans = (ans + D[N - 1][i]) % MOD;
  }
  
  cout << ans;
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
  
}