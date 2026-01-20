/*
[9466: 텀 프로젝트](https://www.acmicpc.net/problem/9466)

Tier: Gold 3
Category: graphs, graph_traversal, dfs
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

#define NOT_VISITED 0
#define VISITED 1
#define IN_CIRCLE 2
#define NOT_IN_CIRCLE 3

ll N;
llv1 ar;
iv1 chk;

int dfs(int idx) {
  // 사이클의 시작지점을 반환한다.
  // 0: 반환은 사이클을 못 찾은 경우 반환한다.

  chk[idx] = VISITED;

  ll nxt = ar[idx];

  if(nxt == idx) {
    // 자기 자신을 가리키는 경우
    chk[idx] = IN_CIRCLE;
    return 0;
  }

  if(chk[nxt] == VISITED) {
    // 다음 노드가 방문 표시되어있는 경우, 사이클에 포함된다.
    chk[idx] = IN_CIRCLE;
    return nxt;
  }

  if(chk[nxt] == IN_CIRCLE || chk[nxt] == NOT_IN_CIRCLE) {
    // 다음 노드가 이미 사이클 판정이 된 경우는 사이클에 포함되지 않는다.
    chk[idx] = NOT_IN_CIRCLE;
    return 0;
  }

  int ret = dfs(nxt);

  if(ret == 0) {
    chk[idx] = NOT_IN_CIRCLE;
    return 0;
  }

  chk[idx] = IN_CIRCLE;
  
  if(ret == idx) {
    // 시작지점에 도착한 경우, 사이클에 대한 결과 전파를 멈춘다.
    return 0;
  }

  return ret;
}

void solve() {
  cin >> N;
  ar.clear();
  ar.resize(N + 1);

  chk.clear();
  chk.resize(N + 1, NOT_VISITED);

  for1(1, N + 1) {
    cin >> ar[i];
  }

  for1(1, N + 1) {
    if(chk[i] == NOT_VISITED) {
      dfs(i);
    }
  }
  
  ll ans = 0;
  for1(1, N + 1) {
    if(chk[i] == 3) ans++;
  }
  cout << ans << "\n";

}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; cin >> tc;
  while(tc--) solve();
  
}
