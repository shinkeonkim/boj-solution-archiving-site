/*
[8111: 0과 1](https://www.acmicpc.net/problem/8111)

Tier: Platinum 5
Category: math, graphs, graph_traversal, bfs
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

void solve() {
  ll N; 
  cin >> N;

  pll ret = {-1, -1};

  llv2 from = llv2(N + 1, llv1(110, 0));
  llv1 dp(N);
  queue <pll> Q;

  // 숫자, 자릿수
  Q.push({1, 1});
  from[1][1] = -1;

  while(!Q.empty()) {
    pll front = Q.front(); Q.pop();
    ll current = front.first;
    ll cnt = front.second;

    if(current % N == 0) {
      ret = front;
      break;
    }
    
    if(cnt == 100) {
      break;
    }

    for(int d = 0; d < 2; d++) {
      ll nxt = (current * 10 + d) % N;

      if(dp[nxt]) continue;
      
      dp[nxt] = 1;
      from[nxt][cnt + 1] = current;
      Q.push({ nxt, cnt + 1});
    }
  }

  if(ret.first == -1) {
    cout << "BRAK";
    return;
  }

  string ans = "";

  while (ret.second > 0) {
    ll current = ret.first;
    ll cnt = ret.second;

    if((from[current][cnt] * 10) % N == current) ans = "0" + ans;
    else ans = "1" + ans;

    ret = { from[current][cnt], cnt - 1};
  }

  cout << ans << "\n";

}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; cin >> tc;
  while(tc--) solve();
  
}
