#include <bits/stdc++.h>

using namespace std;

int V, E, a, b, ans;
vector <int> adj[110];
bool check[110];

void dfs(int here) {
  check[here] = true;

  for(int there : adj[here]) {
    if(!check[there]) {
      dfs(there);
    }
  }
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);

  cin >> V >> E;

  for(int i = 0; i < E; i++) {
    cin >> a >> b;
    adj[a].push_back(b);
    adj[b].push_back(a);
  }

  dfs(1);

  for(int i = 2; i <= V; i++) {
    if(check[i]) ans++;
  }

  cout << ans;
}
