#include <bits/stdc++.h>

#define for1(s,n) for(int i = s; i < n; i++)
#define for1j(s,n) for(int j = s; j < n; j++)
#define foreach(k) for(auto i : k)
#define foreachj(k) for(auto j : k)
#define pb(a) push_back(a)
#define sz(a) a.size()
#define INF 1000000000LL

using namespace std;
typedef unsigned long long ull;
typedef long long ll;
typedef vector <int> iv1;
typedef vector <vector<int> > iv2;
typedef vector <ll> llv1;
typedef unsigned int uint;
typedef vector <ull> ullv1;
typedef vector <vector <ull> > ullv2;

struct MCMF {
	struct Edge {
		ll to;
		ll capacity;
		ll cost;
		
		Edge* rev;
		Edge(ll to, ll capacity, ll cost) : to(to), capacity(capacity), cost(cost) {}
	};
	
	ll n;
	ll source, sink;
	vector<vector<Edge *>> graph;
	vector<bool> check;
	vector<ll> distance;
	vector<pair<ll, ll>> from;
	
	MCMF(ll n, ll source, ll sink): n(n), source(source), sink(sink) {
		graph.resize(n);
		check.resize(n);
		from.resize(n, make_pair(-1, -1));
		distance.resize(n);
	};
	
	void add_edge(ll u, ll v, ll cap, ll cost) {
		Edge *ori = new Edge(v, cap, cost);
		Edge *rev = new Edge(u, 0, -cost);
		
		ori->rev = rev;
		rev->rev = ori;
		
		graph[u].push_back(ori);
		graph[v].push_back(rev);
	}
	
	void add_edge_from_src(ll v, ll cap, ll cost) {
		add_edge(source, v, cap, cost);
	}
	
	void add_edge_to_sink(ll u, ll cap, ll cost) {
		add_edge(u, sink, cap, cost);
	}
	
	bool spfa(ll &total_flow, ll &total_cost) {
		fill(check.begin(), check.end(), false);
		fill(distance.begin(), distance.end(), INF);
		fill(from.begin(), from.end(), make_pair(-1, -1));
		
		distance[source] = 0;
		queue <ll> q;
		q.push(source);
		
		while(!q.empty()) {
			ll x = q.front(); q.pop();
			
			check[x] = false;
			
			for(ll i = 0; i < graph[x].size(); i++) {
				Edge* e = graph[x][i];
				ll y = e->to;
				
				if(e->capacity > 0 && distance[x] + e->cost < distance[y]) {
					distance[y] = distance[x] + e->cost;
					from[y] = make_pair(x, i);
					
					if(!check[y]) {
						check[y] = true;
						q.push(y);
					}
				}
				
			}
		}
		
		if(distance[sink] == INF) return false;
		
		ll x = sink;
		ll c = graph[from[x].first][from[x].second]->capacity;
		
		while(from[x].first != -1) {
			if(c > graph[from[x].first][from[x].second]->capacity) {
				c = graph[from[x].first][from[x].second]->capacity;
			}
			x = from[x].first;
		}
		
		x = sink;
		while(from[x].first != -1) {
			Edge* e = graph[from[x].first][from[x].second];
			e->capacity -= c;
			e->rev->capacity += c;
			x = from[x].first;
		}
		
		total_flow += c;
		total_cost += c * distance[sink];
		
		return true;
	}
	
	pair <ll, ll> flow() {
		ll total_flow = 0;
		ll total_cost = 0;
		
		while(spfa(total_flow, total_cost));
		
		return make_pair(total_flow, total_cost);
	}
};

ll in_node(ll i) {
	return i * 2;
}

ll out_node(ll i) {
	return i * 2 + 1;
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	ll n, k, a;
	cin >> n >> k;
	
	ll SRC = 0;
	ll SINK = 2 * n + 8;
	
	MCMF mcmf(2 * n + 9, in_node(SRC), SINK);
	
	for(ll i = 0; i <= n - 1; i++) {
		for(ll j = i + 1; j <= n; j++) {
			cin >> a;
			
			mcmf.add_edge(out_node(i), in_node(j), 1, a);
		}
	}
    
	mcmf.add_edge(in_node(SRC), out_node(SRC), k, 0);

	for(ll i = 1; i <= n; i++) {
		mcmf.add_edge(in_node(i), out_node(i), 1, -INF);
		mcmf.add_edge(out_node(i), SINK, 1, 0);
	}

	mcmf.add_edge_to_sink(out_node(SRC), k, 0);
	
	auto ans =  mcmf.flow();
	
	cout << ans.second + n * INF;
	
}