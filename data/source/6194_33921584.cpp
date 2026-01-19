#include <bits/stdc++.h>

#define for1(s,n) for(int i = s; i<n; i++)
#define for1j(s,n) for(int j = s; j<n; j++)
#define foreach(k) for(auto i : k)
#define foreachj(k) for(auto j : k)
#define pb(a) push_back((a))
#define sz(a) a.size()

using namespace std;
typedef unsigned long long ull;
typedef long long ll;
typedef vector <int> iv1;
typedef vector <vector<int> > iv2;
typedef vector <ll> llv1;
typedef unsigned int uint;
typedef vector <ull> ullv1;
typedef vector <vector <ull> > ullv2;

struct point{
  ll x, y, p=0, q=0;
};

ll N, M, tc;
vector <point> ar;

ll ccw(point p1, point p2, point p3) {
  ll ret = 1ll * (p1.x * p2.y + p2.x * p3.y + p3.x * p1.y - p2.x * p1.y - p3.x * p2.y - p1.x * p3.y);
  return ret > 0 ? 1 : (ret < 0 ? -1 : 0);
}

double distance(point p1, point p2) {
  return sqrt((p1.x-p2.x)*(p1.x-p2.x) + (p1.y-p2.y)*(p1.y-p2.y));
}

bool comp(point a, point b) {
  if(a.q * b.p != a.p*b.q) return 1ll * a.q * b.p < a.p * b.q;
  if(a.y != b.y) return a.y < b.y;
  return a.x < b.x;
}

void swapPoint(point a, point b) {
  point tmp;
  tmp = a;
  a = b;
  b= tmp;
}

vector <int> getConvexHull(vector <point>& points) {
  vector <int> stk; stk.clear();

  sort(points.begin(), points.end(), comp);

  for(int x=1; x<points.size(); x++) {
      points[x].p = points[x].x - points[0].x;
      points[x].q = points[x].y - points[0].y;
  }

  if(points.size() == 1) {
    return {0};
  }

  sort(points.begin() + 1, points.end(), comp);

  stk.push_back(0);
  stk.push_back(1);

  for(int next = 2; next < points.size(); next++) {
    while(stk.size() >= 2) {
      int second = stk.back(); stk.pop_back();
      int first = stk.back();
      
      if(ccw(points[first], points[second], points[next]) > 0) {
        stk.push_back(second);
        break;
      }
    }
    stk.push_back(next);
  }

  return stk;
}

void init() {
  ll x, y;

  cin >> N;

  ar.clear();

  for1(0, N) {
    cin >> x >> y;
    ar.push_back({ x, y, 0, 0});
  }
}

int main() {
  ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);

  init();

  vector <int> convex_hull = getConvexHull(ar);

  double ans = 0;

  for(int i = 0; i < convex_hull.size(); i++) {
    ans += distance(ar[convex_hull[i]], ar[convex_hull[(i+1) % convex_hull.size()]]);
  }

  cout << fixed;
  cout.precision(2);
  cout << ans;
}