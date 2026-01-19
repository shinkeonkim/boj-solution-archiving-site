#include <bits/stdc++.h>

#define for1(s, e) for(int i = s; i < e; i++)
#define for1j(s, e) for(int j = s; j < e; j++)
#define foreach(k) for(auto i : k)
#define foreachj(k) for(auto j : k)
#define pb(a) push_back(a)
#define sz(a) a.size()

using namespace std;

typedef unsigned long long ull;
typedef long long ll;
typedef __int128 llll;
typedef unsigned int uint;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef pair<double, double> pdd;
typedef pair<double, int> pdi;
typedef double radian_angle;

const double EPS = 1e-8;
const double PI = acos(-1);

template<typename T>
T sq(T x) { return x * x; }

int sign(ll x) { return x < 0 ? -1 : x > 0 ? 1 : 0; }
int sign(int x) { return x < 0 ? -1 : x > 0 ? 1 : 0; }
int sign(double x) { return abs(x) < EPS ? 0 : x < 0 ? -1 : 1; }

pii operator+(const pii &a, const pii &b) { return pii(a.first + b.first, a.second + b.second); }
pii operator-(const pii &a, const pii &b) { return pii(a.first - b.first, a.second - b.second); }
ll operator^(const pii &a, const pii &b) { return (ll)a.first * b.second - (ll)a.second * b.first; } // 외적
ll operator*(const pii &a, const pii &b) { return (ll)a.first * b.first + (ll)a.second * b.second; } // 내적
pii operator*(const pii &a, const int &r) { return pii(a.first * r, a.second * r); }
pii operator-(const pii &a) { return pii(-a.first, -a.second); }

pdd operator+(const pdd &a, const pdd &b) { return pdd(a.first + b.first, a.second + b.second); }
pdd operator-(const pdd &a, const pdd &b) { return pdd(a.first - b.first, a.second - b.second); }
double operator^(const pdd &a, const pdd &b) { return a.first * b.second - a.second * b.first; } // 외적
double operator*(const pdd &a, const pdd &b) { return a.first * b.first + a.second * b.second; } // 내적
pdd operator*(const pdd &a, const double &r) { return pdd(a.first * r, a.second * r); }
pdd operator-(const pdd &a) { return pdd(-a.first, -a.second); }

double size(pdd x) { return hypot(x.first, x.second); }
double size2(pdd x) { return sq(x.first) + sq(x.second); }
ll size2(pii x) { return sq((ll) x.first) + sq((ll) x.second); }

// Geometry
radian_angle polar(pdd x) { return atan2(x.second, x.first); } // 극 좌표 각도
pdd unit(radian_angle theta) { return pdd(cos(theta), sin(theta)); } // 단위 벡터
pdd norm(pdd a) { return a * (1.0 / size(a)); }
pdd rotate(pdd v, radian_angle theta) { return unit(theta) * v.first + unit(theta + PI / 2) * v.second;}
pdd rotate_90(pdd v) { return pdd(-v.second, v.first); }

void normalize(radian_angle &theta) { 
  while(theta < 0) theta += 2 * PI;
  while(theta >= 2 * PI) theta -= 2 * PI;
}

struct circle {
  circle(pdd o, double r):  o(o), r(r) {}
  circle() {} 

  pdd o;
  double r;
};

int intersect(pdd a, pdd b, pdd u, pdd v, pdd &des) {
  if(abs(b ^ v) < EPS) return 0;
  des = pdd(((a - u) ^ v) / (v ^ b), ((a - u) ^ b) / (v ^ b));
  return 1;
}

int get_circle(pdd p0, pdd p1, pdd p2, circle &des) {
  pdd a = (p0 + p1) * 0.5;
  pdd b = rotate_90(p0 - p1);
  pdd u = (p0 + p2) * 0.5;
  pdd v = rotate_90(p0 - p2);
  pdd R;

  if(!intersect(a, b, u, v, R)) return 0;

  des = circle(a + b * R.first, size(a + b * R.first - p0));
  return 1;
}

circle make_circle(vector<pdd> Q) {
  if(Q.size() == 0) return circle(pdd(0, 0), 0);
  if(Q.size() == 1) return circle(Q[0], 0);

  circle res;

  for(int i = 0; i < Q.size(); i++) {
    swap(Q.back(), Q[i]);

    res = circle((Q[0] + Q[1]) * 0.5, size(Q[0] - Q[1]) / 2);

    bool chk = 1;

    for(pdd c : Q)
      if (size2(c - res.o) > sq(res.r) + EPS) chk = 0;

    if(chk) return res;

    swap(Q.back(), Q[i]);
  }

  get_circle(Q[0], Q[1], Q[2], res);
  return res;
}

circle smallest_circle(vector<pdd> &P, vector<pdd> &Q, int N) {
  circle c = make_circle(Q);

  if(N == 0 || Q.size() >= 3) return c;

  for(int i = 0; i < N; i++) {
    if(size2(c.o - P[i]) > sq(c.r)) {
      Q.push_back(P[i]);
      c = smallest_circle(P, Q, i);
      Q.pop_back();
    }
  }

  return c;
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  cout << fixed;
  cout.precision(2);
  vector<pdd> points;
  vector<pdd> res;
  int N;

  cin >> N;

  for1(0, N) {
    pdd x;
    cin >> x.first >> x.second;
    points.push_back(x);
  }

  circle ans = smallest_circle(points, res, N);

  // cout << ans.o.first << " " << ans.o.second << " " << ans.r;
  cout << ans.r * 2;
}