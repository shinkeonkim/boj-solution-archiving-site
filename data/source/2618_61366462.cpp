#include <bits/stdc++.h>

#define for1(s,n) for(int i = s; i < n; i++)
#define for1j(s,n) for(int j = s; j < n; j++)
#define foreach(k) for(auto i : k)
#define foreachj(k) for(auto j : k)
#define pb(a) push_back(a)
#define sz(a) a.size()
#define INF 100000000

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
	int y, x;
};

struct st {
	Point p;
	Point rev;
	int cost;
};

struct cmp{
    bool operator()(st a, st b){
        return a.cost > b.cost;
    }
};
 

int N;
int C;
Point points[1100];
int D[1100][1100];
Point back[1100][1100];

int dis(Point a, Point b) {
	return abs(a.x - b.x) + abs(a.y - b.y);
}

int main() {
  ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	
	cin >> N >> C;
	
	for(int i = 0; i <= C + 1; i++)
		for(int j = 0; j <= C + 1; j++) D[i][j] = INF;
	
	points[0] = {1, 1};
	points[1] = {N, N};
	
	for(int i = 2; i <= C + 1; i++) cin >> points[i].y >> points[i].x;

	priority_queue <st, vector<st>, cmp> q;
	
	q.push({{0, 1}, {0, 0}, 0});
	
	while(!q.empty()) {
		st here = q.top(); q.pop();
		
		int y = here.p.y;
		int x = here.p.x;
		if(D[y][x] <= here.cost) continue;
		
		D[y][x] = here.cost;
		back[y][x] = here.rev;
		
		int nxt = max(y, x) + 1;
		
		if(nxt > C + 1) continue;
		
		q.push({{y, nxt}, here.p, here.cost + dis(points[x], points[nxt])});
		q.push({{nxt, x}, here.p, here.cost + dis(points[y], points[nxt])});
	}
	
	// for(int i = 0; i <= C + 1; i++) {
	// 	for(int j = 0; j <= C + 1; j++) {
	// 		cout << D[i][j] << " ";
	// 	}
	// 	cout << "\n";
	// }
	
	stack <Point> stk;
	int ans = INF;
	Point s;
	
	
	for(int i = 0; i <= C + 1; i++) {
		if(D[i][C + 1] < ans) {
			ans = D[i][C + 1];
			s = {i, C + 1};
		}
		if(D[C+ 1][i] < ans) {
			ans = D[C + 1][i];
			s = {C + 1, i};
		}
	}
	
	cout << ans << "\n";
	
	while(s.x != 0 || s.y != 0) {
		stk.push(s);
		s = back[s.y][s.x];
	}
	
	while(!stk.empty()) {
		Point here = stk.top();
		stk.pop();
		
		if(stk.empty()) continue;
		
		Point there = stk.top();
		
		if(here.x != there.x) cout << 2;
		else cout << 1;
		cout << "\n";
	}
}