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

const ll MOD = 1e9 + 7;

ll two[1100000];
void solve() {
  ll N;
  string s;
  two[0] = 1;
  for(int i = 1; i < 1000001; i++) {
    two[i] = (two[i - 1] * 2) % MOD;
  }

  cin >> N;
  cin >> s;

  reverse(s.begin(), s.end());


  ll K = 0;
  ll KC = 0;
  ll KCO = 0;
  ll ans = 0;
  for(int i = 0; i < N; i++) {
    if(s[i] == 'K') {
      K = (K + 1) % MOD;
    }
    if(s[i] == 'C') {
      KC = (KC + K) % MOD;
    }

    if(s[i] == 'O') {
      KCO = (KCO + KC) % MOD;
    }

    if(s[i] == 'R') {
      ans = (ans + KCO * two[N - i - 1]) % MOD;
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