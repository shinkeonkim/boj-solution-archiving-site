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
typedef vector <vector<int>> iv2;
typedef vector <ll> llv1;
typedef unsigned int uint;
typedef vector <ull> ullv1;
typedef vector <vector <ull>> ullv2;

ll N, S, D;

llv1 edge[110000];
ll height[110000];
bool check[110000];
ll ans;

ll dfs(ll node, ll h) {
    check[node] = true;
    ll ret = 0;
    for(auto next: edge[node]) {
        if(!check[next]) {
            ret = max(ret, dfs(next, h+1) + 1);
        }
    }
    return height[node] = ret;
}

void travel(ll node, ll h) {
    check[node] = true;
    // cout << node << " ";
    for(auto next: edge[node]) {
        if(!check[next] && height[next] >= D) {
            ans += 2;
            travel(next, h+1);
        }
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    
    cin >> N >> S >> D;
    for1(0, N-1) {
        ll a,b;
        cin >> a >> b;
        edge[a].pb(b);
        edge[b].pb(a);
    }

    dfs(S, 0ll);

    fill(check, check+N+1, false);
    travel(S,0ll);

    cout << ans;
}