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

// D[i][j]
// i번째 계단"까지" 밟았을 때,
// 이전에 j번 계단을 연속해서 밟은 경우, 얻은 최대값

int N;
int ar[330];
int D[330][2];

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);

  cin >> N;

  for(int i = 1; i <= N; i++) cin >> ar[i];

  D[1][0] = ar[1];
  D[1][1] = ar[1];

  for(int i = 2; i <= N; i++) {
    D[i][0] = ar[i] + max(D[i-2][0], D[i-2][1]);
    D[i][1] = ar[i] + D[i-1][0];
  }

  cout << max(D[N][0], D[N][1]);
}