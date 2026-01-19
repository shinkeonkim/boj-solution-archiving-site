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

ull ar[1100];

ull zero(ull a) {
  ull ret = 1;
  if(a == 0) return 10;
  
  while(a > 0) {
    ret *= 10;
    a /= 10;
  }
  return ret;
}

bool compare(ull a, ull b) {
  ull x = a * zero(b) + b;
  ull x2 = b * zero(a) + a;
  
  if(x <= x2) return false;
  return true;
}

void solve() {
  int N;
  
  cin >> N;
  
  for1(0, N) {
    cin >> ar[i];    
  }
  
  sort(ar, ar+N, compare);
  
  if(ar[0] == 0) {
    cout << 0;
    return;
  }
  
  for1(0, N) {
    cout << ar[i];
  }
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
}
