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
const ll INF = 1e13;

template<typename T>
T sq(T x) { return x * x; }

ll N, V, E;
ll A, B;
vector<ll> places;
vector <pll> edges[1100];

vector<ll> dijkstra(ll start) {
  vector<ll> ret;
  ret.resize(V + 1, INF);
  
  priority_queue <pll, vector<pll>, less<pll>> Q;
  
  Q.push(make_pair(0, start));
  
  while(!Q.empty()) {
    auto f = Q.top();
    
    Q.pop();
    
    ll cost = f.first;
    ll here = f.second;
    
    if(cost >= ret[here]) continue;
    
    ret[here] = cost;
    
    for(auto nxt : edges[here]) {
      if(ret[nxt.second] <= cost + nxt.first) continue;
      
      Q.push(make_pair(cost + nxt.first, nxt.second));
    }
  }
  
  
  return ret;
}


void solve() {
  cin >> N >> V >> E;
  
  cin >> A >> B;
  
  places.resize(N);
  
  for1(0, N) cin >> places[i];
  
  for1(0, E) {
    ll a, b, l;
    cin >> a >> b >> l;
    
    edges[a].push_back({l, b});
    edges[b].push_back({l, a});
  }
  
  vector<ll> ret1 = dijkstra(A);
  vector<ll> ret2 = dijkstra(B);
  
  ll ans = 0;

  for1(0, N) {
    ll p = places[i];
    ll d1 = ret1[p] == INF ? -1 : ret1[p]; 
    ll d2 = ret2[p] == INF ? -1 : ret2[p];
    
    ans += d1 + d2;    
  }
  
  cout << ans;
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
  
}