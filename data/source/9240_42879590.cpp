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

struct Point {
  ll x, y;
  ll p = 0;
  ll q = 0;

  Point diffPoint(Point a) {
    return Point({ x - a.x, y - a.y, 0, 0 });
  }

  ll dist(Point a) {
    return (x - a.x) * (x - a.x) + (y - a.y) * (y - a.y);
  }
};

bool comp1(Point a, Point b) {
  if(a.y != b.y) return a.y < b.y;
  return a.x < b.x;
}

// tan 기준으로 정렬하기 위한 비교 함수
bool comp2(Point a, Point b) {
  if(a.q * b.p != a.p * b.q) return a.q * b.p < a.p * b.q;
  return comp1(a, b);
}

ll ccw(Point p1, Point p2, Point p3) {
    ll ret = (p1.x * p2.y + p2.x * p3.y + p3.x * p1.y - p2.x * p1.y - p3.x * p2.y - p1.x * p3.y);
    return ret;
}

int C;
vector <Point> ar;
stack <int> stk;
vector <Point> convexHull;

int main() {
  ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);
  cout << fixed;
  cout.precision(7);
  
  cin >> C;
  Point tmp;

  for1(0, C) {
    cin >> tmp.x >> tmp.y;
    ar.push_back(tmp);
  }

  sort(ar.begin(), ar.end(), comp1);

  for(int x = 1; x < C; x++) {
    ar[x].p = ar[x].x - ar[0].x;
    ar[x].q = ar[x].y - ar[0].y;
  }

  sort(ar.begin()+1, ar.end(), comp2);

  stk.push(0);
  stk.push(1);

  int nxt = 2;

  while(nxt < ar.size()) {
    while(stk.size() >= 2) {
      int second = stk.top();
      stk.pop();
      int first = stk.top();

      if(ccw(ar[first], ar[second], ar[nxt]) > 0) {
        stk.push(second);
        break;
      }
    }
    stk.push(nxt++);
  }

  while(!stk.empty()) {
    convexHull.push_back(ar[stk.top()]);
    stk.pop();
  }

  reverse(convexHull.begin(), convexHull.end());

  // rotating calipers

  ll ans = 0, sz = convexHull.size();
  int i = 0, j = 1;

  for(i = 0; i < sz; i++) {
    int iNxt = (i + 1) % sz;
    while(1) {
      int jNxt = (j + 1) % sz;

      Point tanI = convexHull[iNxt].diffPoint(convexHull[i]);
      Point tanJ = convexHull[jNxt].diffPoint(convexHull[j]);
      
      if (ccw({0, 0}, tanI, tanJ) <= 0) break;
      j = jNxt;
    }

    ll d = convexHull[i].dist(convexHull[j]);

    ans = max(ans, d);
  }

  cout << sqrt(ans);
}