/*
[32514: 최단 경로 아니면 음수 사이클](https://www.acmicpc.net/problem/32514)

Tier: Platinum 5
Category: graphs, shortest_path, bellman_ford
*/


#include <bits/stdc++.h>

using namespace std;

#define forn(i, s, e) for(int (i)=s; (i) < e; (i)++)
#define forEach(i, k) for(auto (i) : k)
#define sz(vct) vct.size()
#define all(vct) vct.begin(), vct.end()
#define sortv(vct) sort(vct.begin(), vct.end())
#define uniq(vct) sort(all(vct));vct.erase(unique(all(vct)), vct.end())
#define fi first
#define se second
#define INF 987654321

typedef unsigned long long ull;
typedef long long ll;
typedef ll llint;
typedef unsigned int uint;
typedef unsigned long long int ull;
typedef ull ullint;

typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef pair<double, double> pdd;
typedef pair<double, int> pdi;
typedef pair<string, string> pss;

typedef vector<int> iv1;
typedef vector<iv1> iv2;
typedef vector<ll> llv1;
typedef vector<llv1> llv2;

typedef vector<pii> piiv1;
typedef vector<piiv1> piiv2;
typedef vector<pll> pllv1;
typedef vector<pllv1> pllv2;
typedef vector<pdd> pddv1;
typedef vector<pddv1> pddv2;

const double EPS = 1e-8;
const double PI = acos(-1);

template<typename T>
T sq(T x) { return x * x; }

int sign(ll x) { return x < 0 ? -1 : x > 0 ? 1 : 0; }
int sign(int x) { return x < 0 ? -1 : x > 0 ? 1 : 0; }
int sign(double x) { return abs(x) < EPS ? 0 : x < 0 ? -1 : 1; }

int N, M, start;
vector <pii> adj[22000];
iv1 D;
iv1 previous;
int cycleStart;

struct BellmanFord {
  void addEdge(int s, int e, int cost) {
    adj[s].push_back({e, cost});
  }

  bool run(int start_point) {
    // 음수 간선 cycle 유무를 반환합니다.
    // 거리 정보는 D 벡터에 저장됩니다.
    // O(V * E)
    D[start_point] = 0;
  
    bool isCycle = false;

    forn(i, 0, N) {
      forn(j, 1, N + 1) {
        for(int k=0; k < sz(adj[j]); k++) {
          pii p = adj[j][k];
          int end = p.first;
          int dist = D[j] + p.second;

          if (D[j] != INF && D[end] > dist) {
            D[end] = dist;
            previous[end] = j;
          }
        }
      }
    }

    forn(j, 1, N + 1) {
      for(int k=0; k < sz(adj[j]); k++) {
        pii p = adj[j][k];
        int end = p.first;
        int dist = D[j] + p.second;

        if (D[j] != INF && D[end] > dist) {
          isCycle = true;
          cycleStart = end;
          return isCycle;
        }
      }
    }
    return isCycle;
  }

  iv1 getPath(int s, int e) {
    vector<int> ret;
    int current = e;
    while(current != -1) {
      ret.push_back(current);
      current = previous[current];
    }
    reverse(ret.begin(), ret.end());
    return ret;
  }
  
  iv1 getCyclePath(int start) {
    vector<int> ret;

    int current = start;

    for(int i = 0; i < N; i++) {
      current = previous[current];
    }

    start = current;

    while(true) {
      ret.push_back(current);
      current = previous[current];
      if(current == start) break;
    }
    ret.push_back(start);
    reverse(ret.begin(), ret.end());
    return ret;
  }

  iv1 getCyclePath() {
    return getCyclePath(cycleStart);
  }
};


void solve() {
  BellmanFord bf; // 1-index BF

  cin >> N >> M >> start; start++;
  D.resize(N + 1, INF);
  previous.resize(N + 1, -1);

  forn(i, 0, M) {
    int a, b, c;
    cin >> a >> b >> c; a++; b++;
    bf.addEdge(a, b, c);
  }

  bool isCycle = bf.run(start);

  if(isCycle) {
    cout << "CYCLE\n";
    
    iv1 cyclePath = bf.getCyclePath();
    
    cout << sz(cyclePath) - 1 << "\n";
    for(auto v : cyclePath) {
      cout << v - 1 << " ";
    }
  } else {
    cout << "PATH\n";

    forn(i, 1, N + 1) {
      // 모든 정점까지의 경로가 존재하므로, INF 케이스는 없다.
      cout << D[i] << " ";
    }
  }
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
  
}
