#include <bits/stdc++.h>

#define for1(s,n) for(int i = s; i < n; i++)
#define for1j(s,n) for(int j = s; j < n; j++)
#define foreach(k) for(auto i : k)
#define foreachj(k) for(auto j : k)
#define pb(a) push_back(a)
#define sz(a) a.size()

using namespace std;
typedef unsigned long long ull;
typedef long long ll;
typedef vector <int> iv1;
typedef vector <vector<int> > iv2;
typedef vector <ll> llv1;
typedef unsigned int uint;
typedef vector <ull> ullv1;
typedef vector <vector <ull> > ullv2;

ll n, m, r, s, e;
llv1 edges[110000];
bool check[110000];
int ans[110000];
int cnt = 1;

void dfs(int crt) {
  check[crt] = true;
  ans[crt] = cnt++;

  for(ll nxt : edges[crt]) {
    if(check[nxt]) continue;

    dfs(nxt);
  }
}

int main() {
  ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);
  cin >> n >> m >> r;

  for1(0, m) {
    cin >> s >> e;

    edges[s].push_back(e);
    edges[e].push_back(s);
  }

  for1(1, n+1) {
    sort(edges[i].begin(), edges[i].end());
  }

  dfs(r);

  for1(1, n+1) {
    cout << ans[i] << "\n";
  }
}