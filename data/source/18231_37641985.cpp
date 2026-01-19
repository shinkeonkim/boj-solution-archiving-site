#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

ll N, M, a, b, K;

vector<ll> adj[2200];
bool fired[2200];
bool chk[2200];
bool ans[2200];

int main() {
  cin >> N >> M;

  for(int i = 0; i < M; i++) {
    cin >> a >> b;
    a--;
    b--;
    adj[a].push_back(b);
    adj[b].push_back(a);
  }

  cin >> K;

  for(int i = 0; i < K; i++) {
    cin >> a;
    fired[--a] = 1;
  }

  for(int i = 0; i < N; i++) {
    if(fired[i]) {
      bool tmp = 1;
      for(auto j : adj[i]) {
        if(!fired[j]) tmp = 0;
      }
      if(tmp) {
        ans[i] = 1;
        chk[i] = 1;
        for(auto j : adj[i]) {
          chk[j] = 1;
        }
      }
    }
  }

  for(int i = 0; i < N; i++) {
    if(chk[i] != fired[i]) {
      cout << -1;
      return 0;
    }
  }

  int cnt = 0;

  for(int i = 0; i < N; i++) {
    if(ans[i]) {
      cnt++;
    }
  }

  cout << cnt << "\n";

  for(int i = 0; i < N; i++) {
    if(ans[i]) {
      cout << i + 1 << " ";
    }
  }
}