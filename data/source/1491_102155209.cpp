/*
[1491: 나선](https://www.acmicpc.net/problem/1491)

Tier: Silver 4
Category: implementation, simulation
*/


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

typedef vector<bool> bv1;
typedef vector<bv1> bv2;

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

ll N, M;
bv2 chk;
pll start;
pll current;
ll d = 0;

ll dx[] = {1, 0, -1, 0};
ll dy[] = {0, 1, 0, -1};

void solve() {
  cin >> M >> N;

  start = { 0, 0 }; 
  chk = bv2(N, bv1(M, false));

  current = start;
  for(int i = 0; i < N * M - 1; i++) {
    auto [y, x] = current;
    // cout << y << "  " << x  << "\n";
    chk[y][x] = true;

    ll ny = y + dy[d];
    ll nx = x + dx[d];
    
    if(ny < 0 || nx < 0 || ny >= N || nx >= M || chk[ny][nx]) {
      d = (d + 1) % 4;

      ny = y + dy[d];
      nx = x + dx[d];
    }

    current = { ny, nx };
  }

  cout << current.second << " " << current.first;
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
}
