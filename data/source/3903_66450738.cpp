#include <bits/stdc++.h>

#define for1(s,n) for(int i = s; i < n; i++)
#define for1j(s,n) for(int j = s; j < n; j++)
#define foreach(k) for(auto i : k)
#define foreachj(k) for(auto j : k)
#define pb(a) push_back(a)
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
typedef long double ld;

const double eps = 1e-9, inf = 1e9;

struct Point {
  ld x, y;
  
  explicit Point(ld x = 0, ld y = 0) : x(x), y(y) {}
  
  friend Point operator + (const Point& p, const Point& q) {
    return Point(p.x + q.x, p.y + q.y);
  }

  friend Point operator - (const Point& p, const Point& q) {
    return Point(p.x - q.x, p.y - q.y);
  }
  
  friend Point operator * (const Point& p, ld k) {
    return Point(p.x * k, p.y * k);
  }
  
  friend ld dot(const Point& p, const Point& q) {
    return p.x * q.x + p.y * q.y;
  }
  
  friend ld cross(const Point& p, const Point& q) {
    return p.x * q.y - p.y * q.x;
  }
};

struct HalfPlane {
  Point p, pq;
  // p : 지나가는 점, pq: 방향벡터
  
  ld angle;
  
  HalfPlane() {}
  HalfPlane(const Point &a, const Point &b) : p(a), pq(b - a) {
    angle = atan2l(pq.y, pq.x);
  }
  HalfPlane(const Point &p, const Point &pq, const ld& angle) : p(p), pq(pq), angle(angle) {}
  
  bool out(const Point& r) {
    return cross(pq, r - p) < -eps;
  }
  
  bool operator < (const HalfPlane& e) const {
    return angle < e.angle;
  }
  
  friend Point inter(const HalfPlane& s, const HalfPlane& t) {
    long double alpha = cross((t.p - s.p), t.pq) / cross(s.pq, t.pq);
    return s.p + (s.pq * alpha);
  }
};

vector<Point> hp_intersect(vector<HalfPlane>& H) {
  // Point box[4] = {
  //   Point(inf, inf),
  //   Point(-inf, inf),
  //   Point(-inf, -inf),
  //   Point(inf, -inf),
  // };
  
  // for1(0, 4) {
  //   HalfPlane aux(box[i], box[(i + 1) % 4]);
  //   H.push_back(aux);
  // }
  
  sort(H.begin(), H.end());
  deque<HalfPlane> dq;
  
  int len = 0;
  for(int i = 0; i < int(H.size()); i++) {
    while(len > 1 && H[i].out(inter(dq[len - 1], dq[len - 2]))) {
      dq.pop_back();
      --len;
    }
    while(len > 1 && H[i].out(inter(dq[0], dq[1]))) {
      dq.pop_front();
      --len;
    }
    
    if(len > 0 && fabsl(cross(H[i].pq, dq[len - 1].pq)) < eps) {
      if(dot(H[i].pq, dq[len - 1].pq) < 0.0) return vector<Point> ();
      
      if(H[i].out(dq[len - 1].p)) {
        dq.pop_back();
        --len;
      }
      
      continue;
    }
    
    dq.push_back(H[i]);
    ++len;
  }
  
  while(len > 2 && dq[0].out(inter(dq[len - 1], dq[len - 2]))) {
    dq.pop_back();
    --len;
  }
  while(len > 2 && dq[len - 1].out(inter(dq[0], dq[1]))) {
    dq.pop_front();
    --len;
  }

  if(len < 3) return vector <Point> ();
  
  vector<Point> ret(len);
  for(int i = 0; i + 1 < len; i++) {
    ret[i] = inter(dq[i], dq[i + 1]);
  }
  ret.back() = inter(dq[len - 1], dq[0]);
  return ret;
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
  
  cout << fixed;
  cout.precision(6);
  
  int N;
  
  while(1) {
    cin >> N;
    
    if(N == 0) break;
    
    vector<Point> points;
    points.resize(N);
    
    for1(0, N) {
      cin >> points[i].x >> points[i].y;
    }
    
    vector<HalfPlane> hp;
    
    for1(0, N) {
      hp.push_back(HalfPlane(points[i], points[(i + 1) % N]));
    }
    
    ld s = 0;
    ld e = inf;
    ld ans = 0;
    while(e - s > eps) {
      ld mid = (s + e) / 2;
      vector<HalfPlane> hp2;
      
      for1(0, N) {
        Point df = Point(0, 0);
        ld a = hp[i].pq.x;
        ld b = hp[i].pq.y;
        
        df.x = -b * mid / sqrt(a * a + b * b);
        df.y = a * mid / sqrt(a * a + b * b);
        
        Point last = hp[i].p + df;
        hp2.push_back(HalfPlane(hp[i].p + df, hp[i].pq, hp[i].angle));  
      }
      
      vector<Point> ret = hp_intersect(hp2);
      
      if(ret.size() == 0) {
        e = mid - 0.00000001;
      } else {
        s = mid + 0.00000001;
        ans = max(ans, mid);
      }
    }
    
    cout << ans << "\n";
  }
}