#include <bits/stdc++.h>

#define MAX_V 200010
#define INF (ll)1e18

using namespace std;
typedef long long ll;

struct edge {
	int node;
	ll cost;
	bool operator<(const edge &to) const {
		return cost > to.cost;
	}
};

ll dist[MAX_V + 1];
ll link[MAX_V + 1];
ll linkr[MAX_V + 1];
vector<edge> adj[MAX_V + 1];
vector<int> start;

void dijkstra(int n) {
	fill(dist, dist + n + 1, INF);
	priority_queue<edge> pq;
    for(int i=0; i<start.size(); i++){
        pq.push({start[i], 0});
        dist[start[i]] = 0;
    }
	while (!pq.empty()) {
		edge cur = pq.top();
		pq.pop();

		if (cur.cost > dist[cur.node]) continue;

		for (int i=0; i < adj[cur.node].size(); i++){
            edge nxt = adj[cur.node][i];
            if(dist[cur.node] + nxt.cost < dist[nxt.node])
                linkr[nxt.node]--;
        }
        for(int i=0; i<adj[cur.node].size(); i++){
            edge nxt = adj[cur.node][i];
            if(link[nxt.node] - linkr[nxt.node] >= (int)(link[nxt.node]+1)/2 && dist[cur.node] + nxt.cost < dist[nxt.node]){
                dist[nxt.node] = dist[cur.node] + nxt.cost;
                pq.push({ nxt.node, dist[nxt.node] });
            }
        }
	}
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	
	int v, e, b, m;
	cin >> v;
    fill(link, link + v + 1, 0);
    fill(linkr, linkr + v + 1, 0);
	for (int i = 1; i <= v; i++) {
        while(1){
            cin >> b;
            if(b==0) break;
            adj[i].push_back({b, 1});
            link[i]++;
            linkr[i]++;
        }
	}
    cin >> m;
    while(m--){
        cin >> b;
        start.push_back(b);
    }
	dijkstra(v);
    for(int i=1;i<=v; i++){
        if(dist[i]==INF) cout << -1 << " ";
        else cout << dist[i] << " ";
    }
    cout << endl;
}