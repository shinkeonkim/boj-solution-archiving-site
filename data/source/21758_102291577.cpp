/*
[21758: 꿀 따기](https://www.acmicpc.net/problem/21758)

Tier: Gold 5
Category: greedy, prefix_sum
*/


#include <bits/stdc++.h>

using namespace std;

#define forn(i, s, e) for(int (i)=s; (i) < e; (i)++)
#define forEach(i, k) for(auto (i) : k)
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
llv1 ar;
llv1 prefixSum;

ll getSum(int start, int end) {
  if(end < start) return 0;
  return prefixSum[end] - prefixSum[start - 1];
}

void initPrefixSum() {
  forn(i, 1, N + 1) {
    prefixSum[i] = prefixSum[i - 1] + ar[i];
  }
  prefixSum[N+1] = prefixSum[N];
}

ll solution() {
  initPrefixSum();
  ll ans = 0;
  ll totalSum = getSum(1, N);

  ll mx = 0;

  for(int i = 2; i <= N; i++) {
    // i : 또다른 벌 스타트 지점
    // 벌통을 사이에 둔다면
    ll ret = getSum(2, i - 1) + mx; // 벌통을 최대값을 가진 지점으로 설정한다면
    ans = max(ans, ret);
    mx = max(mx, ar[i]);
    
    // 벌통을 오른쪽에 끝에 두었다 가정
    if(i == N) continue; // 불가능 케이스
    ret = (getSum(2, N) - ar[i]) + getSum(i + 1, N);
    ans = max(ans, ret);
  }

  return ans;
}

void solve() {
  cin >> N;
  ar.resize(N + 1);
  prefixSum.resize(N + 2);

  forn(i, 1, N + 1) {
    cin >> ar[i];
  }

  ll ans1 = solution();

  reverse(ar.begin() + 1, ar.end());

  ll ans2 = solution();
  
  cout << max(ans1, ans2);
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
}
