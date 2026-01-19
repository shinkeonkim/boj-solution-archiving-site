#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

struct Vtor {
	ll x, y;
	ll p = 0, q = 0;
	
	explicit Vtor(ll _x = 0 ,ll _y = 0) : x(_x), y(_y) {}
	
	Vtor operator- (const Vtor &a) const {
		return Vtor(x - a.x, y - a.y);
	}
	
	double cross(const Vtor &a) const {
		return x * a.y - a.x * y;
	}
};

bool comp1(Vtor a, Vtor b) {
	if(a.y != b.y) return a.y < b.y;
	return a.x < b.x;
}

bool comp2(Vtor a, Vtor b) {
	if(a.q * b.p != a.p * b.q) return a.q * b.p < a.p * b.q;
	return comp1(a, b);
}

double ccw(Vtor a, Vtor b) {
	return a.cross(b);
}

double ccw(Vtor a, Vtor b, Vtor p) {
	return ccw(a - p, b - p);
}

vector<Vtor> get_convex_hull_points(ll N, vector<Vtor>& points) {
	sort(points.begin(), points.end(), comp1);
	
	for(int i = 1; i < N; i++) {
		points[i].p = points[i].x - points[0].x;
		points[i].q = points[i].y - points[0].y;
	}
	
	sort(points.begin(), points.end(), comp2);
	
	vector<ll> stk;
	stk.push_back(0);
	stk.push_back(1);
	
	int nxt = 2;
	while(nxt < N) {
		while(stk.size() >= 2) {
			int s = stk.back();
			stk.pop_back();
			int f = stk.back();
			
			if(ccw(points[f], points[s], points[nxt]) > 0) {
				stk.push_back(s);
				break;
			}
		}
		stk.push_back(nxt++);
	}
	
	vector<Vtor> ret;
	
	for(ll i : stk) {
		ret.push_back(points[i]);
	}
	
	return ret;
}


int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	
	ll N;
	Vtor Z;
	vector<Vtor> points;

	cin >> N;
	
	for(int i = 0; i < N; i++) {
		cin >> Z.x >> Z.y;
		points.push_back(Z);
	}
	
	vector<Vtor> ret = get_convex_hull_points(N, points);
	
	cout << ret.size();
}