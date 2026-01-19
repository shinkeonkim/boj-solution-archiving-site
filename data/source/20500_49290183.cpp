#include <bits/stdc++.h>

#define for1(s,n) for(int i = s; i < n; i++)
#define for1j(s,n) for(int j = s; j < n; j++)
#define foreach(k) for(auto i : k)
#define foreachj(k) for(auto j : k)
#define pb(a) push_back(a)
#define sz(a) a.size()
#define MAX_N 1515
#define MOD 1000000007

using namespace std;
typedef unsigned long long ull;
typedef long long ll;
typedef vector <int> iv1;
typedef vector <vector<int> > iv2;
typedef vector <ll> llv1;
typedef unsigned int uint;
typedef vector <ull> ullv1;
typedef vector <vector <ull> > ullv2;

ll N;
ll D[1555][3];
// D[i][j] 1과 5로 이루어진 i 자리의 숫자를 3으로 나누었을 때 나머지가 j인 개수를 기록한다.

int main() {
  ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);

  cin >> N;

  D[1][0] = 0;
  D[1][1] = 1;
  D[1][2] = 1;

  for(int i = 2; i <= MAX_N; i++) {
    for(int j = 0; j < 3; j++) {
      D[i][j] = (D[i-1][(j+1)%3] + D[i-1][(j+2)%3]) % MOD;
    }
  }

  cout << D[N-1][1];
}