#include <bits/stdc++.h>

#define for1(s,n) for(int i = s; i < n; i++)
#define for1j(s,n) for(int j = s; j < n; j++)

using namespace std;

string s;
int d[1100], ans;

int main() {
  ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);
  
  cin >> s;

  int n = s.length();

  for1(0, n) d[i] = 1;

  for1(1, n) {
    for1j(0, i) {
      if((i - j) % 2 && s[i] == s[j]) {
        d[i] = max(d[i], d[j] + 1);
      }
    }
  }

  for1(0, n) {
    ans = max(d[i], ans);
  }

  cout << ans;
}
