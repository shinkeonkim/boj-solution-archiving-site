#include <bits/stdc++.h>

#define for1(s,n) for(int i = s; i < n; i++)
#define for1j(s,n) for(int j = s; j < n; j++)
#define foreach(k) for(auto i : k)
#define foreachj(k) for(auto j : k)
#define pb(a) push_back(a)
#define sz(a) a.size()

#define MAX_N 220000
#define MAX_E 1100000

using namespace std;
typedef unsigned long long ull;
typedef long long ll;
typedef vector <int> iv1;
typedef vector <vector<int> > iv2;
typedef vector <ll> llv1;
typedef unsigned int uint;
typedef vector <ull> ullv1;
typedef vector <vector <ull> > ullv2;

int groups[MAX_N];
ll N, M, a, b, c, cnt;
double result;

struct Edge {
	int here, there;
	double cost;
	
	Edge(): Edge(0, 0, -1) {}
	Edge(ll h, ll t, double c): here(h), there(t), cost(c) {}
	
	bool operator <(const Edge& e) const { return cost < e.cost; }
};

int find(int a) {
	if(groups[a] < 0) return a;
	return groups[a] = find(groups[a]);
}

bool merge(int a, int b) {
	a = find(a);
	b = find(b);
	
	if(a == b) return false;
	groups[b] = a;
	
	return true;
}

Edge edges[MAX_E];
double x[110];
double y[110];

double dist(int a, int b) {
	return sqrt((x[a] - x[b]) * (x[a] - x[b]) + (y[a] - y[b]) * (y[a] - y[b])); 
}

int main() {
  ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	
	cin >> N;
		
	for1(0, N) {
		cin >> x[i] >> y[i];
	}
	
	for1(0, N) {
		for1j(i + 1, N) {
			edges[M++] = Edge(i, j, dist(i, j));
		}
	}
	
	sort(edges, edges+M);
	fill(groups, groups + N, -1);
	
	for(int i = 0; ; i++) {
		if(cnt >= N - 1) break;

		if(merge(edges[i].here, edges[i].there)) {
			result += edges[i].cost;
			cnt++;
		}
	}
	
	cout << fixed;
	cout.precision(2);
	
	cout << result;
}