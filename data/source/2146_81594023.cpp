/*
[2146: 다리 만들기](https://www.acmicpc.net/problem/2146)

Tier: Gold 3 
Category: bfs, graphs, graph_traversal
여러 섬으로 이루어진 나라가 있다. 이 나라의 대통령은 섬을 잇는 다리를 만들겠다는 공약으로 인기몰이를 해 당선될 수 있었다. 하지만 막상 대통령에 취임하자, 다리를 놓는다는 것이 아깝다는 생각을 하게 되었다. 그래서 그는, 생색내는 식으로 한 섬과 다른 섬을 잇는 다리 하나만을 만들기로 하였고, 그 또한 다리를 가장 짧게 하여 돈을 아끼려 하였다.

이 나라는 N×N크기의 이차원 평면상에 존재한다. 이 나라는 여러 섬으로 이루어져 있으며, 섬이란 동서남북으로 육지가 붙어있는 덩어리를 말한다. 다음은 세 개의 섬으로 이루어진 나라의 지도이다.



위의 그림에서 색이 있는 부분이 육지이고, 색이 없는 부분이 바다이다. 이 바다에 가장 짧은 다리를 놓아 두 대륙을 연결하고자 한다. 가장 짧은 다리란, 다리가 격자에서 차지하는 칸의 수가 가장 작은 다리를 말한다. 다음 그림에서 두 대륙을 연결하는 다리를 볼 수 있다.



물론 위의 방법 외에도 다리를 놓는 방법이 여러 가지 있으나, 위의 경우가 놓는 다리의 길이가 3으로 가장 짧다(물론 길이가 3인 다른 다리를 놓을 수 있는 방법도 몇 가지 있다).

지도가 주어질 때, 가장 짧은 다리 하나를 놓아 두 대륙을 연결하는 방법을 찾으시오.

입력
첫 줄에는 지도의 크기 N(100이하의 자연수)가 주어진다. 그 다음 N줄에는 N개의 숫자가 빈칸을 사이에 두고 주어지며, 0은 바다, 1은 육지를 나타낸다. 항상 두 개 이상의 섬이 있는 데이터만 입력으로 주어진다.

출력
첫째 줄에 가장 짧은 다리의 길이를 출력한다.

예제 입력 1 
10
1 1 1 0 0 0 0 1 1 1
1 1 1 1 0 0 0 0 1 1
1 0 1 1 0 0 0 0 1 1
0 0 1 1 1 0 0 0 0 1
0 0 0 1 0 0 0 0 0 1
0 0 0 0 0 0 0 0 0 1
0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 1 0 0 0 0
0 0 0 0 1 1 1 0 0 0
0 0 0 0 0 0 0 0 0 0
예제 출력 1 
3
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

ll N;
llv2 board, dist;
ll dy[] = { 0, 0, 1, -1 };
ll dx[] = { 1, -1, 0, 0 };

void solve() {
  cin >> N;
  board.resize(N, llv1(N));
  dist.resize(N, llv1(N, INF));

  queue <pll> Q;

  for1(0, N) {
    for1j(0, N) {
      cin >> board[i][j];
    }
  }

  vector<vector<bool>> chk(N, vector<bool>(N, false));

  ll area_num = 2;
  for1(0, N) {
    for1j(0, N) {
      if(board[i][j] && !chk[i][j]) {
        Q.push({ i, j });
        chk[i][j] = true;

        while(!Q.empty()) {
          auto [y, x] = Q.front(); Q.pop();
          board[y][x] = area_num;

          for(int d = 0; d < 4; d++) {
            ll ny = y + dy[d];
            ll nx = x + dx[d];

            if(ny < 0 || nx < 0 || ny >= N || nx >= N) continue;
            if(chk[ny][nx]) continue;
            if(board[ny][nx] == 0) continue;
            
            chk[ny][nx] = true;
            Q.push({ny, nx});
          }
        }

        area_num++;
      }
    }
  }

  chk = vector<vector<bool>>(N, vector<bool>(N, false));


  for1(0, N) {
    for1j(0, N) {
      if(board[i][j] != 0) {
        Q.push({ i, j });
        chk[i][j] = true;
        dist[i][j] = 0;
      }
    }
  }

  while(!Q.empty()) {
    auto [y, x] = Q.front(); Q.pop();

    for(int d = 0; d < 4; d++) {
      ll ny = y + dy[d];
      ll nx = x + dx[d];

      if(ny < 0 || nx < 0 || ny >= N || nx >= N) continue;
      if(chk[ny][nx]) continue;
      if(board[ny][nx] >= 2) continue;
      board[ny][nx] = board[y][x];
      dist[ny][nx] = dist[y][x] + 1;
      
      chk[ny][nx] = true;
      Q.push({ny, nx});
    }
  }

  ll ans = INF;

  for1(0, N) {
    for1j(0, N) {
      if(i + 1 < N) {
        if(board[i][j] != board[i+1][j]) ans = min(ans, dist[i][j] + dist[i+1][j]);
      }
      if(j + 1 < N) {
        if(board[i][j] != board[i][j+1]) ans = min(ans, dist[i][j] + dist[i][j+1]);
      }
    }
  }

  cout << ans;

}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
  
}