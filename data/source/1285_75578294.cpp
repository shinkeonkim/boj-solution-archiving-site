#include <bits/stdc++.h>

using namespace std;

#define for1(s, e) for(int i = s; i < e; i++)
#define for1j(s, e) for(int j = s; j < e; j++)
#define forEach(k) for(auto i : k)
#define forEachj(k) for(auto j : k)
#define sz(vct) a.size())
#define all(vct) vct.begin(), vct.end()
#define uniq(vct) sort(all(vct));vct.erase(unique(all(vct)), vct.end())
#define fi first
#define se second

typedef unsigned long long ull;
typedef long long ll;
typedef __int128 llll;
typedef unsigned int uint;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef pair<double, double> pdd;
typedef pair<double, int> pdi;
typedef pair<string, string> pss;

const int INF = 987654321;

int ans = INF;
std::mt19937_64 seed(112981);
std::uniform_real_distribution<double> rng(0, 1);

int n;
int ar[32][32];
int original[32][32];

void backup() {
  for(int i = 0; i < n; i++) {
    for(int j = 0; j < n; j++) original[i][j] = ar[i][j];
  }
}

void restore() {
  for(int i = 0; i < n; i++) {
    for(int j = 0; j < n; j++) ar[i][j] = original[i][j];
  }
}

void print() {
  for(int i = 0; i < n; i++) {
    for(int j = 0; j < n; j++) cout << ar[i][j] << " ";
    cout << "\n";
  }
  cout << "\n";

}

int scoring() {
  int ret = 0;
  for(int i = 0; i < n; i++) {
    for(int j = 0; j < n; j++) {
      ret += ar[i][j];
    }
  }
  return ret;
}

void turn(int y, int x) {
  if(x == 0) {
    for(int i = 0; i < n; i++) {
      ar[y][i] = 1 - ar[y][i];
    }
  } else {
    for(int i = 0; i < n; i++) {
      ar[i][x] = 1 - ar[i][x];
    }
  }
}

void column_turn() {
  for(int i = 0; i < n; i++) {
    int cnt = 0;
    for(int j = 0; j < n; j++) {
      if(ar[j][i] == 1) cnt++;
    }

    if(cnt * 2 > n) {
      turn(0, i);
    }
  }
}

double t = 1, d=0.9999, k = 10 ,lim = 0.0005;
/*
  t: 현재 온도
  d: 온도
  k: 볼츠만 상수
  lim: 언제까지?
*/

void simulated_anealing() {
  double e1, e2; // e1: 현재 상태, e2: 다음 상태

  while(t > lim) {
    e1 = scoring();

    backup();
    // 1 -> 2로 변경
    int pos = rand() % n;
    turn(pos, 0);
    column_turn();

    e2 = scoring();

    double p = exp((e1 - e2) / (k * t));

    if(p < rng(seed)) {
      // 2 -> 1 로 원복
      restore();
    }

    t *= d;
    ans = min(ans, scoring());
  }
}

void solve() {
  string s;

  cin >> n;

  for1(0, n) {
    cin >> s;

    for1j(0, n) {
      ar[i][j] = (s[j] == 'T' ? 1 : 0);
    }
  }

  simulated_anealing();

  cout << ans;
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
}