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

ll R, C;
ll ans = 0;
vector <string> ar;

// 각 틀마다 나올 수 있는 조각을 1부터 4까지 정해놓는다.

// O는 위에서 봤을때
// 1 2
// 3 4

// I는 정면에서 봤을때
// 1 2
// 3 4

// H는 오른쪽에서 봤을 때
// 1 2
// 3 4

// 각 틀마다 원래 나올 수 있는 석고 조각의 개수는 4개
// O와 O가 만나면 왼쪽의 2번 / 오른쪽의 1번 합쳐짐. 왼쪽의 4번 / 오른쪽의 3번 합쳐짐.



ll node_number(ll y, ll x, ll k) {
  return (y * C + x) * 5 + k;
}

struct UnionFind {
  ll n;
  vector<ll> u;

  UnionFind(ll n) : n(n) {
    u.resize(n + 1);
    for(ll i = 1; i <= n; i++) {
      u[i] = i;
    }
  }

  ll find(ll k) {
    if(u[u[k]] == u[k]) return u[k];
    else return u[k]=find(u[k]);
  }

  void uni(ll a, ll b) {
    a = find(a);
    b = find(b);
    if(a < b) u[b] = a;
    else u[a] = b; 
  }
};


void solve() {
  cin >> R >> C;
  ar.resize(R);

  UnionFind uf(R * C * 6 + 10);

  for1(0, R) cin >> ar[i];

  for1(0, R) {
    for1j(0, C) {
      if(ar[i][j] == 'O') {
        // 가로 배치
        if(j + 1 < C) {
          if(ar[i][j + 1] == 'O') {
            uf.uni(node_number(i, j, 2), node_number(i, j + 1, 1));
            uf.uni(node_number(i, j, 4), node_number(i, j + 1, 3));
          } else if(ar[i][j + 1] == 'I') {
            uf.uni(node_number(i, j, 2), node_number(i, j, 4));
            uf.uni(node_number(i, j, 2), node_number(i, j + 1, 1));
            uf.uni(node_number(i, j, 2), node_number(i, j + 1, 3));
          } else if(ar[i][j + 1] == 'H') {
            uf.uni(node_number(i, j, 2), node_number(i, j + 1, 2));
            uf.uni(node_number(i, j, 2), node_number(i, j + 1, 4));
            uf.uni(node_number(i, j, 4), node_number(i, j + 1, 1));
            uf.uni(node_number(i, j, 4), node_number(i, j + 1, 3));
          }
        }

        // 세로 배치
        if(i + 1 < R) {
          if(ar[i + 1][j] == 'O') {
            uf.uni(node_number(i, j, 3), node_number(i + 1, j, 1));
            uf.uni(node_number(i, j, 4), node_number(i + 1, j, 2));
          }
          else if(ar[i + 1][j] == 'I') {
            uf.uni(node_number(i, j, 3), node_number(i + 1, j, 1));
            uf.uni(node_number(i, j, 3), node_number(i + 1, j, 3));
            uf.uni(node_number(i, j, 4), node_number(i + 1, j, 2));
            uf.uni(node_number(i, j, 4), node_number(i + 1, j, 4));
          }
          else if(ar[i + 1][j] == 'H') {
            uf.uni(node_number(i, j, 3), node_number(i, j, 4));
            uf.uni(node_number(i, j, 3), node_number(i + 1, j, 2));
            uf.uni(node_number(i, j, 3), node_number(i + 1, j, 4));
          }
        }
      }

      else if(ar[i][j] == 'I') {
        if(j + 1 < C) {
          if(ar[i][j + 1] == 'O') {
            uf.uni(node_number(i, j, 2), node_number(i, j, 4));
            uf.uni(node_number(i, j, 2), node_number(i, j + 1, 1));
            uf.uni(node_number(i, j, 2), node_number(i, j + 1, 3));
          }
          if(ar[i][j + 1] == 'I') {
            uf.uni(node_number(i, j, 2), node_number(i, j + 1, 1));
            uf.uni(node_number(i, j, 4), node_number(i, j + 1, 3));
          }
          if(ar[i][j + 1] == 'H') {
            uf.uni(node_number(i, j, 2), node_number(i, j + 1, 1));
            uf.uni(node_number(i, j, 2), node_number(i, j + 1, 2));
            uf.uni(node_number(i, j, 4), node_number(i, j + 1, 3));
            uf.uni(node_number(i, j, 4), node_number(i, j + 1, 4));
          }
        }
        if(i + 1 < R) {
          if(ar[i + 1][j] == 'O') {
            uf.uni(node_number(i, j, 1), node_number(i + 1, j, 1));
            uf.uni(node_number(i, j, 3), node_number(i + 1, j, 1));

            uf.uni(node_number(i, j, 2), node_number(i + 1, j, 2));
            uf.uni(node_number(i, j, 4), node_number(i + 1, j, 2));
          }
          else if(ar[i + 1][j] == 'I') {
            uf.uni(node_number(i, j, 1), node_number(i + 1, j, 1));
            uf.uni(node_number(i, j, 2), node_number(i + 1, j, 2));
            uf.uni(node_number(i, j, 3), node_number(i + 1, j, 3));
            uf.uni(node_number(i, j, 4), node_number(i + 1, j, 4));
          }
          else if(ar[i + 1][j] == 'H') {
            uf.uni(node_number(i, j, 1), node_number(i + 1, j, 2));
            uf.uni(node_number(i, j, 2), node_number(i + 1, j, 2));
            uf.uni(node_number(i, j, 3), node_number(i + 1, j, 4));
            uf.uni(node_number(i, j, 4), node_number(i + 1, j, 4));
          }

        }
      }

      if(ar[i][j] == 'H') {
        if(j + 1 < C) {
          if(ar[i][j + 1] == 'O') {
            uf.uni(node_number(i, j, 2), node_number(i, j + 1, 1));
            uf.uni(node_number(i, j, 4), node_number(i, j + 1, 1));

            uf.uni(node_number(i, j, 1), node_number(i, j + 1, 3));
            uf.uni(node_number(i, j, 3), node_number(i, j + 1, 3));
          }
          else if(ar[i][j + 1] == 'I') {
            uf.uni(node_number(i, j, 1), node_number(i, j + 1, 1));
            uf.uni(node_number(i, j, 2), node_number(i, j + 1, 1));

            uf.uni(node_number(i, j, 3), node_number(i, j + 1, 3));
            uf.uni(node_number(i, j, 4), node_number(i, j + 1, 3));
          }
          else if(ar[i][j + 1] == 'H') {
            uf.uni(node_number(i, j, 1), node_number(i, j + 1, 1));
            uf.uni(node_number(i, j, 2), node_number(i, j + 1, 2));
            uf.uni(node_number(i, j, 3), node_number(i, j + 1, 3));
            uf.uni(node_number(i, j, 4), node_number(i, j + 1, 4));
          }
        }
        if(i + 1 < R) {
          if(ar[i + 1][j] == 'O') {
            uf.uni(node_number(i, j, 1), node_number(i, j, 3));
            uf.uni(node_number(i, j, 1), node_number(i + 1, j, 1));
            uf.uni(node_number(i, j, 1), node_number(i + 1, j, 2));
          }
          else if(ar[i + 1][j] == 'I') {
            uf.uni(node_number(i, j, 1), node_number(i + 1, j, 1));
            uf.uni(node_number(i, j, 1), node_number(i + 1, j, 2));

            uf.uni(node_number(i, j, 3), node_number(i + 1, j, 3));
            uf.uni(node_number(i, j, 3), node_number(i + 1, j, 4));
          }
          else if(ar[i + 1][j] == 'H') {
            uf.uni(node_number(i, j, 1), node_number(i + 1, j, 2));
            uf.uni(node_number(i, j, 3), node_number(i + 1, j, 4));
          }
        }
      }
    }  
  }

  set <ll> s;
  
  for1(0, R) {
    for1j(0, C) {
      for(ll k = 1; k <= 4; k++) {
        s.insert(uf.find(node_number(i, j, k)));
      }
    }
  }

  cout << sz(s);
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(NULL);cout.tie(NULL);
  int tc = 1; // cin >> tc;
  while(tc--) solve();
}
