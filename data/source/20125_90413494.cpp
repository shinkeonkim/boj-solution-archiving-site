#include <bits/stdc++.h>

using namespace std;

#define for1(s, e) for(int i = s; i < e; i++)
#define for1j(s, e) for(int j = s; j < e; j++)
#define forEach(k) for(auto i : k)
#define forEachj(k) for(auto j : k)
#define sz(vct) vct.size()
#define all(vct) vct.begin(), vct.end()
#define sortv(vct) sort(vct.begin(), vct.end())
#define uniq(vct) sort(all(vct));vct.erase(unique(all(vct)), vct.end())
#define fi first
#define se second
#define INF (1ll << 60ll)

typedef unsigned long long ull;
typedef long long ll;
typedef ll llint;
typedef unsigned int uint;
typedef unsigned long long int ull;
typedef ull ullint;

typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef pair<double, double> pdd;
typedef pair<double, int> pdi;
typedef pair<string, string> pss;

typedef vector<int> iv1;
typedef vector<iv1> iv2;
typedef vector<ll> llv1;
typedef vector<llv1> llv2;

typedef vector<pii> piiv1;
typedef vector<piiv1> piiv2;
typedef vector<pll> pllv1;
typedef vector<pllv1> pllv2;
typedef vector<pdd> pddv1;
typedef vector<pddv1> pddv2;

const double EPS = 1e-8;
const double PI = acos(-1);

template<typename T>
T sq(T x) { return x * x; }

int sign(ll x) { return x < 0 ? -1 : x > 0 ? 1 : 0; }
int sign(int x) { return x < 0 ? -1 : x > 0 ? 1 : 0; }
int sign(double x) { return abs(x) < EPS ? 0 : x < 0 ? -1 : 1; }

void solve() {
  ll n;
  vector<string> ar;

  cin >> n;
  ar.resize(n);

  for1(0, n) {
    cin >> ar[i];
  }

  pii center;

  for1(1, n-1) {
    for1j(1, n-1) {
      if (ar[i][j] == '*' && ar[i-1][j] == '*' && ar[i+1][j] == '*' && ar[i][j-1] == '*' && ar[i][j+1] == '*') {
        center = {i, j};
      }
    }
  }

  int left_arm = 0;
  int right_arm = 0;
  int body = 0;
  int left_leg = 0;
  int right_leg = 0;

  for(int i = center.se - 1; i > -1; i--) {
    if(ar[center.fi][i] != '*') break;
    left_arm++;
  }

  for(int i = center.se + 1; i < n; i++) {
    if(ar[center.fi][i] != '*') break;
    right_arm++;
  }

  for(int i = center.fi + 1; i < n; i++) {
    if(ar[i][center.se] != '*') break;
    body++;
  }

  int body_last_y = center.fi + body;

  for(int i = body_last_y + 1; i < n; i++) {
    if(ar[i][center.se - 1] != '*') break;
    left_leg++;
  }

  for(int i = body_last_y + 1; i < n; i++) {
    if(ar[i][center.se + 1] != '*') break;
    right_leg++;
  }

  cout << center.fi + 1 << " " << center.se + 1 << "\n";
  cout << left_arm << " " << right_arm << " " << body << " " << left_leg << " " << right_leg;
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
}
