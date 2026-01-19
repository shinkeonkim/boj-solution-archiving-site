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
ll a;
ll cnt[4400];

ll f(ll v) {
  ll ret = 0;
  
  while(v > 0) {
    ll last = v % 10;
    
    ret |= (1 << last);
    
    v /= 10;
  }
  
  return ret;
}

void solve() {
  cin >> N;
  
  for1(0, N) {
    cin >> a;
    
    cnt[f(a)]++;
  }
  
  ll ans = 0;
  for(int i = 0; i < (1 << 10); i++) ans += cnt[i] * (cnt[i] - 1) / 2LL;
  
  for(int i = 0; i < (1 << 10); i++) {
    for(int j = i + 1; j < (1 << 10); j++) {
      if((i & j) == 0) continue;

      ans += cnt[i] * cnt[j];
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