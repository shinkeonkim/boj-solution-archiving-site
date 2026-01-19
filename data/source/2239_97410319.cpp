/*
[2239: 스도쿠](https://www.acmicpc.net/problem/2239)

Tier: Gold 4 
Category: implementation, backtracking
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

bool row[9][10], col[9][10], square[9][10];
int board[9][9];

int to_sq(int y, int x) {
  return (y / 3) * 3 + (x / 3);
}

void input() {
  for1(0, 9) {
    for1j(0, 9) {
      scanf("%1d", &board[i][j]);
      if(board[i][j]) {
        row[i][board[i][j]] = true;
        col[j][board[i][j]] = true;
        square[to_sq(i, j)][board[i][j]] = true;
      }
    }
  }
}

void dfs(int idx) {
  int y = idx / 9;
  int x = idx % 9;

  if(idx == 81) {
    for1(0, 9) {
      for1j(0, 9) {
        cout << board[i][j];
      }
      cout << '\n';
    }
    exit(0);
  }

  if(board[y][x]) {
    dfs(idx + 1);
  } else {
    for1(1, 10) {
      if(!row[y][i] && !col[x][i] && !square[to_sq(y, x)][i]) {
        row[y][i] = col[x][i] = square[to_sq(y, x)][i] = true;
        board[y][x] = i;
        dfs(idx + 1);
        board[y][x] = 0;
        row[y][i] = col[x][i] = square[to_sq(y, x)][i] = false;
      }
    }
  }
}

void solve() {
  input();
  dfs(0);
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
  
}
