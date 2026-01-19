/*
[12100: 2048 (Easy)](https://www.acmicpc.net/problem/12100)

Tier: Gold 1 
Category: backtracking, bruteforcing, implementation, simulation
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

ll n;
ll dy[] = { 0, 0, 1, -1 };
ll dx[] = { 1, -1, 0, 0 };

llv2 move(int direction, llv2 b) {
  llv2 board = b;

  if(direction < 2) {
    // 0: right, 1: left
    if(direction == 0) {
      for(int y = 0; y < n; y++) {
        for(int x = n - 2; x >= 0; x--) {
          if(board[y][x] == 0) {
            board[y][x] = board[y][x + 1];
            board[y][x + 1] = 0;
          }

          if(board[y][x] == board[y][x + 1]) {
            board[y][x + 1] *= 2; 
            board[y][x] = 0;
          }
        }

        // 한쪽면으로 압축
        llv1 tmp;
        for(int x = 0; x < n; x++) {
          if(board[y][x] != 0) {
            tmp.push_back(board[y][x]);
          }
        }

        for(int x = 0; x < n; x++) {
          if(x < tmp.size()) {
            board[y][n - x - 1] = tmp[tmp.size() - x - 1];
          } else {
            board[y][n - x - 1] = 0;
          }
        }
      }
    } else {
      for(int y = 0; y < n; y++) {
        for(int x = 1; x < n ; x++) {
          if(board[y][x] == 0) {
            board[y][x] = board[y][x - 1];
            board[y][x - 1] = 0;
          }

          if(board[y][x] == board[y][x - 1]) {
            board[y][x] = 0;
            board[y][x - 1] *= 2;
          }
        }

        // 한쪽면으로 압축
        llv1 tmp;

        for(int x = 0; x < n; x++) {
          if(board[y][x] != 0) {
            tmp.push_back(board[y][x]);
          }
        }

        for(int x = 0; x < n; x++) {
          if(x < tmp.size()) {
            board[y][x] = tmp[x];
          } else {
            board[y][x] = 0;
          }
        }
      }
    }
    
  } else {
    // 2: down, 3: up

    if(direction == 2) {
      for(int x = 0; x < n; x++) {
        for(int y = n - 2; y >= 0; y--) {
          if(board[y][x] == 0) {
            board[y][x] = board[y + 1][x];
            board[y + 1][x] = 0;
          }

          if(board[y][x] == board[y + 1][x]) {
            board[y + 1][x] *= 2;
            board[y][x] = 0;
          }
        }

        // 한쪽면으로 압축
        llv1 tmp;
        for(int y = 0; y < n; y++) {
          if(board[y][x] != 0) {
            tmp.push_back(board[y][x]);
          }
        }

        for(int y = 0; y < n; y++) {
          if(y < tmp.size()) {
            board[n - y - 1][x] = tmp[tmp.size() - y - 1];
          } else {
            board[n - y - 1][x] = 0;
          }
        }
      }
    } else {
      for(int x = 0; x < n; x++) {
        for(int y = 1; y < n; y++) {
          if(board[y][x] == 0) {
            board[y][x] = board[y - 1][x];
            board[y - 1][x] = 0;
          }

          if(board[y][x] == board[y - 1][x]) {
            board[y - 1][x] *= 2;
            board[y][x] = 0;
          } 
        }
        // 한쪽면으로 압축

        llv1 tmp;
        for(int y = 0; y < n; y++) {
          if(board[y][x] != 0) {
            tmp.push_back(board[y][x]);
          }
        }

        for(int y = 0; y < n; y++) {
          if(y < tmp.size()) {
            board[y][x] = tmp[y];
          } else {
            board[y][x] = 0;
          }
        }
      }
    }
  }

  return board;
}

ll get_mx(llv2 board) {
  ll ret = 0;
  for1(0, n) {
    for1j(0, n) {
      ret = max(ret, board[i][j]);
    }
  }
  return ret;
}

ll dfs(int cnt, llv2 board) {
  if(cnt == 5) {
    return get_mx(board);
  }

  ll ret = get_mx(board);

  for(int d = 0; d < 4; d++) {
    llv2 new_board = board;
    new_board = move(d, new_board);
    ret = max(ret, dfs(cnt + 1, new_board));
  }
  
  return ret;
}

void solve() {
  cin >> n;
  llv2 board(n, llv1(n));
  for1(0, n) {
    for1j(0, n) {
      cin >> board[i][j];
    }
  }

  cout << dfs(0, board);
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
  
}