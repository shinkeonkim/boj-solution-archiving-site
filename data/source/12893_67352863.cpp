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

ll N, M;
vector<ll> edges[2200];
ll color[2200];

int ch(int c) {
  if(c == 0) return c;
  return c == 1 ? 2 : 1;
}

bool dfs(int node, int c) {
  if(color[node] != c && color[node] > 0) return false;
  
  bool ret = true;
  color[node] = c;
  
  for(ll there : edges[node]) {
    if(color[there] == ch(c)) continue;
    
    ret = ret && dfs(there, ch(c));
  }
  
  return ret;
}

void solve() {
  cin >> N >> M;
  
  for1(0, M) {
    ll a, b;
    cin >> a >> b;
    
    edges[a].push_back(b);
    edges[b].push_back(a);
  }
  
  for1(1, N + 1) {
    if(color[i] == 0) {
      bool ret = dfs(i, 1);
      
      if(!ret) {
        cout << 0;
        return;
      }
    }
  }
  
  cout << 1;
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
  
}