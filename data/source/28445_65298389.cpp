#include <bits/stdc++.h>

using namespace std;

#define for1(s,n) for(int i = s; i < n; i++)
#define for1j(s,n) for(int j = s; j < n; j++)
#define forEach(k) for(auto i : k)
#define forEachj(k) for(auto j : k)
#define pb(a) push_back(a)
#define sz(a) a.size()
#define all(a) a.begin(), a.end()

typedef pair<string, string> pss;

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);

  vector<pss> ans;

  string ar[4];

  for1(0, 4) cin >> ar[i];

  for1(0, 4) {
    for1j(0, 4) ans.push_back({ar[i], ar[j]});
  }

  sort(all(ans));
  ans.erase(unique(all(ans)), ans.end());

  forEach(ans) {
    cout << i.first << " " << i.second << "\n";
  }
}