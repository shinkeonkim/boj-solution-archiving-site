#include <bits/stdc++.h>

#define for1(s,n) for(int i = s; i < n; i++)
#define for1j(s,n) for(int j = s; j < n; j++)
#define foreach(k) for(auto i : k)
#define foreachj(k) for(auto j : k)
#define pb(a) push_back(a)
#define sz(a) a.size()

#define MX_N 100
#define MX_NODE 2*(MX_N + 1)
#define SRC MX_NODE-2
#define SINK MX_NODE-1
#define INF (ll)1e18

using namespace std;
typedef unsigned long long ull;
typedef long long ll;
typedef vector <int> iv1;
typedef vector <vector<int>> iv2;
typedef vector <ll> llv1;
typedef unsigned int uint;
typedef vector <ull> ullv1;
typedef vector <vector <ull>> ullv2;

ll N, ans;
ll cost[MX_NODE][MX_NODE];
ll capacity[MX_NODE][MX_NODE];
ll flow[MX_NODE][MX_NODE];
llv1 edge[MX_NODE];

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    
    cin >> N;

    for1(0, N) {
        capacity[SRC][i] = 1;
        edge[SRC].pb(i);
        edge[i].pb(SRC);
    }

    for1(N, 2*N) {
        capacity[i][SINK] = 1;
        edge[SINK].pb(i);
        edge[i].pb(SINK);
    }

    for1(0, N) {
        for1j(N, 2*N) {
            capacity[i][j] = 1;
            cin >> cost[i][j];
            cost[j][i] = -cost[i][j];
            edge[i].pb(j);
            edge[j].pb(i);
        }
    }   

    while(1) {
        ll prev[MX_NODE];
        ll dis[MX_NODE];
        bool isInQ[MX_NODE];
        queue <ll> Q;

        fill(prev, prev+MX_NODE, -1);
        fill(dis, dis+MX_NODE, INF);
        fill(isInQ, isInQ+MX_NODE, false);

        dis[SRC] = 0;
        Q.push(SRC);
        isInQ[SRC] = true;

        while(!Q.empty()) {
            ll crt = Q.front();
            Q.pop();

            isInQ[crt] = false;


            for(ll next: edge[crt]) {
                if(capacity[crt][next] - flow[crt][next] > 0 && dis[next] > dis[crt] + cost[crt][next]) {
                    dis[next] = dis[crt] + cost[crt][next];
                    prev[next] = crt;

                    if(!isInQ[next]) {
                        Q.push(next);
                        isInQ[next] = true;
                    }
                }
            }
        }

        if(prev[SINK] == -1) break;

        for(ll i = SINK; i!= SRC; i=prev[i]) {
            ans += cost[prev[i]][i];
            flow[prev[i]][i] += 1;
            flow[i][prev[i]] -= 1;
        }
    }
    cout << ans;

}