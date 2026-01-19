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

const int INF = 987654321;
const int MX = 440000;
int s, e;
int dist[440000];

void solve() {
  // 0-1 BFS 활용
  cin >> s >> e;

  for1(0, MX) dist[i] = INF;
  dist[s] = 0;
  deque <pii> dq;

  dq.push_front({s, 0});

  while(!dq.empty()) {
    pii f = dq.front(); dq.pop_front();

    if(dist[f.fi] < f.se) continue;
    dist[f.fi] = f.se;

    // 이동
    if(f.fi * 2 < MX && f.fi != 0) {
      dq.push_front({f.fi * 2 , f.se});
    }
    if(f.fi + 1 < MX) {
      dq.push_back({f.fi + 1, f.se + 1});
    }
    if(f.fi - 1 >= 0) {
      dq.push_back({f.fi - 1, f.se + 1});
    }
  }
  
  cout << dist[e];
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
}