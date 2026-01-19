#include <bits/stdc++.h>

using namespace std;
int T;
string s;

int main() {
  ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);

  cin >> T;
  while(T--) {
    cin >> s;

    cout << s.front() << s.back() << "\n";
  }
}