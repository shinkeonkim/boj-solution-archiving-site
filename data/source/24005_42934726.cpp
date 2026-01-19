#include <bits/stdc++.h>
#define INF 1111111
using namespace std;

int t, a, ans;
int D[11000];

int main() {
  ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);
  cin >> t;
  D[1] = 1;

  for(int i = 2; i<= 10000; i++) {
    D[i] = INF;
  }

  for(int i = 2; i<= 10000; i++) {
    for(int j = 1; j * j <= i; j++) {
      D[i] = min(D[i], D[i - j*j]+1);
    }
  }
  
  for(int tc = 1; tc<= t; tc++) {
    cin >> a;
    cout << "Case #" << tc << ": " << D[a] << "\n";
  }
}
