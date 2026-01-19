#include <bits/stdc++.h>

#define for1(s,n) for(int i = s; i < n; i++)

using namespace std;
typedef long long ll;

struct edge{
  ll to;
  ll cost;
};

ll N, M, a, b, c, ans;
ll D[1100];
ll track[1100];
vector<edge> edges[1100];
vector<ll> nodes;

void resetNodes(ll from) {
  nodes.clear();
  int c = 1;

  while(c != from) {
    nodes.push_back(c);
    c = track[c];
  }
  nodes.push_back(from);
  nodes.push_back(1);
}

void dfs(ll crt, ll cost, ll from) {
  if(D[crt] >= cost) return;

  if(crt == 1 && from != -1) {
    if(ans < cost) {
      ans = cost;
      resetNodes(from);
    }
    return;
  }

  D[crt] = cost;
  if(from != -1) {
    track[from] = crt;
  }

  for(edge e : edges[crt]) {
    if(D[e.to] < e.cost + cost) {
      dfs(e.to, e.cost + cost, crt);
    }
  }
}

int main() {
  ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);
  cin >> N >> M;

  fill(D, D+N+1, -1);

  for1(0, M) {
    cin >> a >> b >> c;

    edges[a].push_back({ b, c });
  }

  dfs(1, 0, -1);

  cout << ans << "\n";
  for(auto i : nodes) cout << i << " ";
}